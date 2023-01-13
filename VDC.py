# importing wx files
import json
import wx

# import the newly created GUI file
import formVDCmain
import constantVDC
import functionVDC

import os
import sqlite3

# inherit from the MainFrame created in wxFowmBuilder

class VDCFrame(formVDCmain.VDCmain):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        formVDCmain.VDCmain.__init__(self, parent)

        temp = list()
        for x in constantVDC.kategorie:
            temp.append(x[0][0:1] + ". " + x[1])
        self.ComboBoxKategoriaMV.Append(list(dict.fromkeys(temp)))
        self.ComboBoxKategoriaMV.SetSelection(2)
        self.ComboBoxKategoriaMVOnChoice(None)
        self.ComboBoxPodkategoriaMV.SetSelection(2)
        self.ComboBoxPodkategoriaMVOnChoice(None)
        self.ComboBoxPalivo.Append(constantVDC.palivo)

        temp.clear()
        for x in constantVDC.poskodeniek2[1:]:
            temp.append(x[0])
        self.ComboBoxKPV_poskodenie.Append(temp)
        self.ComboBoxKPV_poskodenie.SetSelection(0)

        # test data
        self.TextBoxDatumPU.SetValue("08.03.2021")
        self.TextBoxVprevadzkeOd.SetValue("18.07.2015")
        self.TextBoxOdjazdene.SetValue("134 782")
        self.TextBoxHV_VHV.SetValue("12 500,00")
        self.TextBoxKPV_K5Zdroj1.SetValue("1")
        self.TextBoxKPV_K5VHV1.SetValue("12 500,00")
        self.TextBoxKPV_K5vPrevadzke1.SetValue("01.01.2015")
        self.TextBoxKPV_K5km1.SetValue("130 000")
        self.TextBoxKPV_K5Cena1.SetValue("1 000,00")
        # test data end

        functionVDC.VypocitajDobuPrevadzky(self)

    def NovyVypocet(self, event):
        for item in vars(self).items():
            if (item[0][0:7] == "TextBox"):
                item[1].SetValue("")
            if (item[0][0:8] == "ComboBox"):
                item[1].SetStringSelection("")
            if (item[0][0:8] == "CheckBox"):
                item[1].SetValue(False)

        self.ComboBoxKategoriaMV.SetSelection(2)
        self.ComboBoxKategoriaMVOnChoice(None)
        functionVDC.VypocitajDobuPrevadzky(self)

    def OtvorZoSuboru(self, event):
        with wx.FileDialog(self, "VDC JSON file", wildcard="VDC JSON files (*.vdcJSON)|*.vdcJson",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'r') as json_file:
                    functionVDC.SetVDCdata(self, json.load(json_file))                    
            except IOError:
                wx.LogError("Cannot open file '%s'." % pathname)
            except Exception as err:
                wx.MessageBox("Error: " + err.__str__(), "Attention",
                              wx.ICON_ERROR | wx.OK, self)

    def ButtonUlozitToFileOnButtonClick(self, event):
        with wx.FileDialog(self, "Save VDC JSON file", wildcard="VDC JSON files (*.vdcJSON)|*.vdcJson",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'w') as file:
                    json.dump(functionVDC.GetVDCdata(self), file, ensure_ascii=False)
            except IOError:
                wx.LogError(
                    "Cannot save current data in file '%s'." % pathname)
            except Exception as err:
                wx.MessageBox("Error: " + err.__str__(), "Attention",
                              wx.ICON_ERROR | wx.OK, self)

    def ButtonNNO_TlacOnButtonClick(self, event):
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Spacer
        from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.lib import colors

        with wx.FileDialog(self, "Save PDF file", wildcard="PDF files (*.pdf)|*.pdf",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            pathname = fileDialog.GetPath()
            try:
                my_doc = SimpleDocTemplate(pathname, rightMargin=40, leftMargin=40)
                pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
                sample_style_sheet = getSampleStyleSheet()
                sample_style_sheet.add(ParagraphStyle(
                    name='Heading1Center', parent=sample_style_sheet['Heading1'], fontName='Arial', alignment=TA_CENTER))
                sample_style_sheet.add(ParagraphStyle(
                    name='Heading1Left', parent=sample_style_sheet['Heading1'], fontName='Arial'))
                sample_style_sheet.add(ParagraphStyle(
                    name='Heading3Left', parent=sample_style_sheet['Heading3'], fontName='Arial'))
                sample_style_sheet.add(ParagraphStyle(
                    name='NormalText', parent=sample_style_sheet['Normal'], fontName='Arial'))
                sample_style_sheet.add(ParagraphStyle(
                    name='TabHeader', parent=sample_style_sheet['Normal'], fontName='Arial', fontSize=7, alignment=TA_CENTER))
                sample_style_sheet.add(ParagraphStyle(
                    name='TabTextRight', parent=sample_style_sheet['Normal'], fontName='Arial', fontSize=8, alignment=TA_RIGHT))
                sample_style_sheet.add(ParagraphStyle(
                    name='TabTextLeft', parent=sample_style_sheet['Normal'], fontName='Arial', fontSize=8, alignment=TA_LEFT))
                flowables = []
                flowables.append(Paragraph("Výpočet všeobecnej hodnoty",
                                sample_style_sheet['Heading1Center']))
                flowables.append(Spacer(1, 5))
                flowables.append(Paragraph("Číslo poistnej udalosti: " +
                                self.TextBoxCPU.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("Dátum vzniku poistnej udalosti: " +
                                self.TextBoxDatumPU.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("Poškodený: " + self.TextBoxPoskodeny.GetValue() + "; " + self.TextBoxPoskodenyAdresa.GetValue() +
                                "; Plátca DPH: " + ("Áno" if self.CheckBoxPlatcaDPH.IsChecked() else "Nie"), sample_style_sheet['NormalText']))
                flowables.append(Spacer(1, 30))

                flowables.append(
                    Paragraph("Vozidlo", sample_style_sheet['Heading1Left']))
                flowables.append(Spacer(1, 5))
                flowables.append(Paragraph("Evidenčné číslo vozidla: " + self.TextBoxECV.GetValue() +
                                "; Evidenčné číslo pridelené po prvý raz: " + self.TextBoxPrideleneECV.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("Kategória vozidla: " +
                                self.ComboBoxKategoriaMV.GetStringSelection(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("Podkategória vozidla: " +
                                self.ComboBoxPodkategoriaMV.GetStringSelection(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("Značka, model, typ: " +
                                self.TextBoxZnackaMV.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("Výrobné číslo vozidla - VIN (Vehicle Identification Number): " +
                                self.TextBoxVIN.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("Technický preukaz číslo: " +
                                self.TextBoxCisloTP.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("Objem valcov motora (ccm): " +
                                self.TextBoxObjemMotora.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("Výkon  (kW): " + self.TextBoxVykon.GetValue() +
                                "; Pri otáčkach: " + self.TextBoxOtacky.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("Výrobné číslo motora: " +
                                self.TextBoxCisloMotora.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("Výrobné číslo rámu: " +
                                self.TextBoxCisloRamu.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph(
                    "Palivo: " + self.ComboBoxPalivo.GetStringSelection(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("Celková hmotnosť (kg): " + self.TextBoxHmotnostCelkova.GetValue() +
                                "; Pohotovostná hmotnosť (kg): " + self.TextBoxPohotovostnaHmotnost.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("Počet náprav / kolies: " +
                                self.TextBoxPocetNaprav.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("Celková dĺžka (mm): " +
                                self.TextBoxCelkovaDlzka.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph(
                    "Rázvor (mm): " + self.TextBoxRazvor.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("Počet dverí / miest: " +
                                self.TextBoxPocetDveri.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("Počet odjazdených km (motohodín) celkom: " +
                                self.TextBoxOdjazdene.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("Farba laku karosérie: " +
                                self.TextBoxFarba.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("Rok výroby / modelový rok: " + self.TextBoxRokVyrobyMV.GetValue() +
                                "; Dátum prvého uvedenia vozidla do prevádzky: " + self.TextBoxVprevadzkeOd.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Spacer(1, 10))

                flowables.append(
                    Paragraph("Pneumatiky", sample_style_sheet['Heading3Left']))
                data = [[Paragraph('Počet', sample_style_sheet['TabHeader']),
                        Paragraph('Značka / rozmer / popis',
                                sample_style_sheet['TabHeader']),
                        Paragraph('Priama TH %', sample_style_sheet['TabHeader']),
                        Paragraph('Nový dezén (mm)', sample_style_sheet['TabHeader']),
                        Paragraph('Nameraný (mm)', sample_style_sheet['TabHeader']),
                        Paragraph('TH %', sample_style_sheet['TabHeader'])]]

                for i in range(1, 4):
                    exec('''if self.TextBoxPneuPocet''' + str(i) + '''.GetValue() != "":
                    data.append([Paragraph(self.TextBoxPneuPocet''' + str(i) + '''.GetValue(), sample_style_sheet['TabTextRight']), 
                                Paragraph(self.TextBoxPneuPopis''' + str(i) + '''.GetValue(), sample_style_sheet['TabTextLeft']), 
                                Paragraph(self.TextBoxPneuPriamaTH''' + str(i) + '''.GetValue(), sample_style_sheet['TabTextRight']), 
                                Paragraph(self.TextBoxPneuNove''' + str(i) + '''.GetValue(), sample_style_sheet['TabTextRight']), 
                                Paragraph(self.TextBoxPneuNamerane''' + str(i) + '''.GetValue(), sample_style_sheet['TabTextRight']), 
                                Paragraph(self.TextBoxPneuTH''' + str(i) + '''.GetValue(), sample_style_sheet['TabTextRight'])])''')

                data.append(["",
                            "",
                            "",
                            "",
                            "",
                            Paragraph(self.TextBoxPneuTH.GetValue(), sample_style_sheet['TabTextRight'])])

                t = Table(data, colWidths=[my_doc.width*8/100,
                                        my_doc.width*28/100,
                                        my_doc.width*16/100,
                                        my_doc.width*16/100,
                                        my_doc.width*16/100,
                                        my_doc.width*16/100])
                t.setStyle(TableStyle(
                    [('GRID', (0, 0), (-1, -2), 1, colors.black),
                    ('GRID', (-1, -1), (-1, -1), 1, colors.black)]))  # (column, row)
                flowables.append(t)

                flowables.append(Spacer(1, 30))

                flowables.append(
                    Paragraph("Technický stav vozidla (TSV) %", sample_style_sheet['Heading1Left']))
                flowables.append(Spacer(1, 5))
                flowables.append(Paragraph("T - doba prevádzky v mesiacoch = " +
                                        self.TextBoxTHdobaPrevadzky.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("PKV - predpokladaný ročný jazdný výkon v km resp. motohodinách = " +
                                        self.TextBoxTHPKV.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("PSKM - počet skutočne najazdených kilometrov = " +
                                        self.TextBoxOdjazdene.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("PZTS - predpokladaný zostatkový technický stav v % = " +
                                        self.TextBoxTHPZTS.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("PEZ - predpokladaná efektívna životnosť v rokoch = " +
                                        self.TextBoxTHPEZ.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("PRKM - Predpokladaný počet najazdených kilometrov = (PKV . T) / 12 = " +
                                        self.TextBoxTHPRKM.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("RKM - Rozdiel v počte najazdených kilometrov (PSKM - PRKM) = " +
                                        self.TextBoxTHRKM.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("kKM - Koeficient najazdených kilometrov = " +
                                        self.TextBoxTHkKM.GetValue(), sample_style_sheet['NormalText']))
                flowables.append(Paragraph("kAM - Koeficient amortizácie za skutočne najazdené kilometre = (RKM . kKM) / 1000 = " +
                                        self.TextBoxTHkAM.GetValue(), sample_style_sheet['NormalText']))

                flowables.append(Spacer(1, 10))

                flowables.append(
                    Paragraph("Tabuľka vypočítaných hodnôt", sample_style_sheet['Heading3Left']))
                data = [[Paragraph('Skupina', sample_style_sheet['TabHeader']),
                        Paragraph('VTSS %', sample_style_sheet['TabHeader']),
                        Paragraph('PDS %', sample_style_sheet['TabHeader']),
                        Paragraph('ZAV %', sample_style_sheet['TabHeader']),
                        Paragraph('ZA %', sample_style_sheet['TabHeader']),
                        Paragraph('ZP %', sample_style_sheet['TabHeader']),
                        Paragraph('TSS %', sample_style_sheet['TabHeader']),
                        Paragraph('PTSS %', sample_style_sheet['TabHeader'])]]

                for i in range(1, 10):
                    exec('''if self.TextBoxTHSkupina''' + str(i) + '''.GetValue() != "":
                    data.append([Paragraph(self.TextBoxTHSkupina''' + str(i) + '''.GetValue(), sample_style_sheet['TabTextLeft']), 
                                Paragraph(self.TextBoxTHVTSS''' + str(i) + '''.GetValue(), sample_style_sheet['TabTextRight']), 
                                Paragraph(self.TextBoxTHPDS''' + str(i) + '''.GetValue(), sample_style_sheet['TabTextRight']), 
                                Paragraph(self.TextBoxTHZAV''' + str(i) + '''.GetValue(), sample_style_sheet['TabTextRight']), 
                                Paragraph(self.TextBoxTHZA''' + str(i) + '''.GetValue(), sample_style_sheet['TabTextRight']), 
                                Paragraph(self.TextBoxTHZP''' + str(i) + '''.GetValue(), sample_style_sheet['TabTextRight']), 
                                Paragraph(self.TextBoxTHTSS''' + str(i) + '''edit.GetValue() + ("*" if self.TextBoxTHTSS'''
                        + str(i) + '''.GetValue() != self.TextBoxTHTSS''' + str(i) + '''edit.GetValue() else ""), sample_style_sheet['TabTextRight']), 
                                Paragraph(self.TextBoxTHPTSS''' + str(i) + '''.GetValue(), sample_style_sheet['TabTextRight'])])''')

                data.append(["",
                            "",
                            "",
                            "",
                            "",
                            "",
                            Paragraph(
                                'TSV:', sample_style_sheet['TabTextRight']),
                            Paragraph(self.TextBoxTHTSV.GetValue(), sample_style_sheet['TabTextRight'])])

                t = Table(data, colWidths=[my_doc.width*29/100,
                                        my_doc.width*11/100,
                                        my_doc.width*10/100,
                                        my_doc.width*10/100,
                                        my_doc.width*10/100,
                                        my_doc.width*10/100,
                                        my_doc.width*10/100,
                                        my_doc.width*10/100])
                t.setStyle(TableStyle(
                    [('GRID', (0, 0), (-1, -2), 1, colors.black),
                    ('GRID', (-1, -1), (-1, -1), 1, colors.black)]))  # (column, row)
                flowables.append(t)

                if (self.TextBoxTHTSS1.GetValue() != self.TextBoxTHTSS1edit.GetValue()
                    or self.TextBoxTHTSS2.GetValue() != self.TextBoxTHTSS2edit.GetValue()
                    or self.TextBoxTHTSS3.GetValue() != self.TextBoxTHTSS3edit.GetValue()
                    or self.TextBoxTHTSS4.GetValue() != self.TextBoxTHTSS4edit.GetValue()
                    or self.TextBoxTHTSS5.GetValue() != self.TextBoxTHTSS5edit.GetValue()
                    or self.TextBoxTHTSS6.GetValue() != self.TextBoxTHTSS6edit.GetValue()
                    or self.TextBoxTHTSS7.GetValue() != self.TextBoxTHTSS7edit.GetValue()
                    or self.TextBoxTHTSS8.GetValue() != self.TextBoxTHTSS8edit.GetValue()
                        or self.TextBoxTHTSS9.GetValue() != self.TextBoxTHTSS9edit.GetValue()):
                    flowables.append(
                        Paragraph("* hodnota zadaná priamo", sample_style_sheet['NormalText']))

                flowables.append(Spacer(1, 10))

                tempVzorec = ""
                if self.LabelTHZAVd.GetLabel() == "":
                    if self.LabelTHZAVa.GetLabel() != "0":
                        tempVzorec += self.LabelTHZAVa.GetLabel() + ' + '
                    if self.LabelTHZAVb.GetLabel() != "0":
                        tempVzorec += 'Odmocnina((T + ' + self.LabelTHZAVb.GetLabel() + \
                            ') / ' + self.LabelTHZAVc.GetLabel() + ')'
                    if self.LabelTHZAVb.GetLabel() == "0":
                        tempVzorec += 'Odmocnina(T / ' + \
                            self.LabelTHZAVc.GetLabel() + ')'
                else:
                    tempVzorec += self.LabelTHZAVd.GetLabel() + ' . T'

                data = [[Paragraph('VTSS - Východiskový technický stav skupiny', sample_style_sheet['TabTextLeft'])],
                        [Paragraph('PDS - Pomerný diel skupiny',
                                sample_style_sheet['TabTextLeft'])],
                        [Paragraph('ZAV - Základná  amortizácia za dobu prevádzky skupiny = ' +
                                tempVzorec, sample_style_sheet['TabTextLeft'])],
                        [Paragraph('ZA - Základná amortizácia = (VTSS - (VTSS / 100 . ZAV)) . kAM / 100 + ZAV',
                                sample_style_sheet['TabTextLeft'])],
                        [Paragraph('ZP - Zrážka, prirážka za technický stav',
                                sample_style_sheet['TabTextLeft'])],
                        [Paragraph('TSS - Skutočný technický stav skupiny = (VTSS . (100 - ZA)) . (100 + ZP) / 10000',
                                sample_style_sheet['TabTextLeft'])],
                        [Paragraph('PTSS - Pomerný technický stav skupiny = (TSS . PDS) / 100',
                                sample_style_sheet['TabTextLeft'])],
                        [Paragraph('TSV - Technický stav vozidla = PTSS1 + ... + PTSSn',
                                sample_style_sheet['TabTextLeft'])],
                        ]

                t = Table(data, colWidths=[my_doc.width])

                t.setStyle(TableStyle(
                    [('GRID', (0, 0), (-1, -1), 1, colors.black)]))  # (column, row)
                flowables.append(t)

                if self.TextBoxHV_VSH.GetValue() != "":
                    flowables.append(Spacer(1, 30))

                    flowables.append(
                        Paragraph("Všeobecná hodnota vozidla (VŠH)", sample_style_sheet['Heading1Left']))
                    flowables.append(Spacer(1, 5))

                    data = [[Paragraph("Východisková hodnota vozidla (VHV)", sample_style_sheet['TabTextLeft']),
                            Paragraph(self.TextBoxHV_VHV.GetValue() + " €", sample_style_sheet['TabTextRight'])],
                            [Paragraph("Technický stav vozidla (TSV)", sample_style_sheet['TabTextLeft']),
                            Paragraph(self.TextBoxHV_TSV.GetValue() + " %", sample_style_sheet['TabTextRight'])],
                            [Paragraph("Východisková  hodnota mimoriadnej výbavy (VHMV)", sample_style_sheet['TabTextLeft']),
                            Paragraph(self.TextBoxHV_VHMV.GetValue() + " €", sample_style_sheet['TabTextRight'])],
                            [Paragraph("Technický stav mimoriadnej výbavy (TSMV)", sample_style_sheet['TabTextLeft']),
                            Paragraph(self.TextBoxHV_TSMV.GetValue() + " %", sample_style_sheet['TabTextRight'])],
                            [Paragraph("Technická hodnota vozidla (TH) = (VHV . TSV) / 100  + (VHVM . TSVM) / 100", sample_style_sheet['TabTextLeft']),
                            Paragraph(self.TextBoxHV_TH.GetValue() + " €", sample_style_sheet['TabTextRight'])]]

                    t = Table(data, colWidths=[my_doc.width*85/100,
                                            my_doc.width*15/100])
                    t.setStyle(TableStyle(
                        [('GRID', (0, 0), (-1, -1), 1, colors.black)]))  # (column, row)
                    flowables.append(t)

                    flowables.append(Spacer(1, 10))

                    flowables.append(
                        Paragraph("Koeficient predajnosti vozidla", sample_style_sheet['Heading3Left']))

                    data = [[Paragraph("k1 - koeficient platnosti kontroly technického stavu vozidla, koniec platnosti TK: " + self.TextBoxKPV_koniecTK.GetValue(), sample_style_sheet['TabTextLeft']),
                            Paragraph(self.TextBoxKPV_K1.GetValue(), sample_style_sheet['TabTextRight'])],
                            [Paragraph("k2 - koeficient poškodenia vozidla haváriou - " + self.ComboBoxKPV_poskodenie.GetStringSelection(), sample_style_sheet['TabTextLeft']),
                            Paragraph(self.TextBoxKPV_K2.GetValue(), sample_style_sheet['TabTextRight'])],
                            [Paragraph("k3 - koeficient počtu držiteľov vozidla, súčasný držiteľ poradie: " + str("Nepreukázané" if self.CheckBoxKPVk3Nezistene.IsChecked() else self.TextBoxKPVPocetDrzitelov.GetValue()), sample_style_sheet['TabTextLeft']),
                            Paragraph(self.TextBoxKPV_K3.GetValue(), sample_style_sheet['TabTextRight'])],
                            [Paragraph("k4 - koeficient spôsobu prevádzky vozidla: " + self.ComboBoxKPV_prevadzka.GetStringSelection(), sample_style_sheet['TabTextLeft']),
                            Paragraph(self.TextBoxKPV_K4.GetValue(), sample_style_sheet['TabTextRight'])],
                            [Paragraph("k5 - koeficient dopytu trhu", sample_style_sheet['TabTextLeft']),
                            Paragraph(self.TextBoxKPV_K5.GetValue(), sample_style_sheet['TabTextRight'])]]

                    t = Table(data, colWidths=[my_doc.width*85/100,
                                            my_doc.width*15/100])
                    t.setStyle(TableStyle(
                        [('GRID', (0, 0), (-1, -1), 1, colors.black)]))  # (column, row)
                    flowables.append(t)

                    flowables.append(Spacer(1, 10))

                    flowables.append(
                        Paragraph("Porovnateľné vozidlá", sample_style_sheet['Heading3Left']))
                    data = [[Paragraph('Zdroj', sample_style_sheet['TabHeader']),
                            Paragraph('VHV', sample_style_sheet['TabHeader']),
                            Paragraph('v prevádzke od',
                                    sample_style_sheet['TabHeader']),
                            Paragraph('km', sample_style_sheet['TabHeader']),
                            Paragraph('Predajná cena',
                                    sample_style_sheet['TabHeader']),
                            Paragraph('TSV', sample_style_sheet['TabHeader']),
                            Paragraph('VHMV', sample_style_sheet['TabHeader']),
                            Paragraph('TSMV', sample_style_sheet['TabHeader']),
                            Paragraph('TH', sample_style_sheet['TabHeader'])]]

                    for i in range(1, 5):
                        exec('''if self.TextBoxKPV_K5Zdroj''' + str(i) + '''.GetValue() != "":
                        data.append([Paragraph(self.TextBoxKPV_K5Zdroj''' + str(i) + '''.GetValue(), sample_style_sheet['TabTextLeft']), 
                                    Paragraph(self.TextBoxKPV_K5VHV''' + str(i) + '''.GetValue() + " €" + ("*" if self.TextBoxKPV_K5VHV'''
                            + str(i) + '''.GetValue() != self.TextBoxHV_VHV.GetValue() else ""), sample_style_sheet['TabTextRight']), 
                                    Paragraph(self.TextBoxKPV_K5vPrevadzke''' + str(i) + '''.GetValue(), sample_style_sheet['TabTextRight']), 
                                    Paragraph(self.TextBoxKPV_K5km''' + str(i) + '''.GetValue(), sample_style_sheet['TabTextRight']), 
                                    Paragraph(self.TextBoxKPV_K5Cena''' + str(i) + '''.GetValue() + " €", sample_style_sheet['TabTextRight']), 
                                    Paragraph(self.TextBoxKPV_K5TSVedit''' + str(i) + '''.GetValue() + " %" + ("*" if self.TextBoxKPV_K5TSV'''
                            + str(i) + '''.GetValue() != self.TextBoxKPV_K5TSVedit''' + str(i) + '''.GetValue() else ""), sample_style_sheet['TabTextRight']), 
                                    Paragraph(self.TextBoxKPV_K5VHMV''' + str(i) + '''.GetValue() + " €", sample_style_sheet['TabTextRight']), 
                                    Paragraph(self.TextBoxKPV_K5TSMV''' + str(i) + '''.GetValue() + " %", sample_style_sheet['TabTextRight']), 
                                    Paragraph(self.TextBoxKPV_K5TH''' + str(i) + '''.GetValue() + " €", sample_style_sheet['TabTextRight'])])''')

                    data.append([Paragraph(
                        "Priemerná predajná cena", sample_style_sheet['TabTextRight']),
                        "",
                        "",
                        "",
                        Paragraph(self.TextBoxKPVpriemPredajCena.GetValue(
                        ) + " €", sample_style_sheet['TabTextRight']),
                        Paragraph(
                        "Priemerná TH vozidiel", sample_style_sheet['TabTextRight']),
                        "",
                        "",
                        Paragraph(self.TextBoxKPVpriemTechHodnVozidla.GetValue() + " €", sample_style_sheet['TabTextRight'])])

                    t = Table(data, colWidths=[my_doc.width*16/100,
                                            my_doc.width*12/100,
                                            my_doc.width*11/100,
                                            my_doc.width*9/100,
                                            my_doc.width*11/100,
                                            my_doc.width*10/100,
                                            my_doc.width*11/100,
                                            my_doc.width*10/100,
                                            my_doc.width*10/100])
                    t.setStyle(TableStyle(
                        [('GRID', (0, 0), (-1, -2), 1, colors.black),
                        ('GRID', (-1, -1), (-1, -1), 1, colors.black),
                        ('GRID', (4, -1), (4, -1), 1, colors.black),
                        ('SPAN', (0, -1), (3, -1)),
                        ('SPAN', (5, -1), (7, -1))]))  # (column, row)
                    flowables.append(t)

                    if (self.TextBoxKPV_K5TSVedit1.GetValue() != self.TextBoxKPV_K5TSV1.GetValue()
                        or self.TextBoxKPV_K5TSVedit2.GetValue() != self.TextBoxKPV_K5TSV2.GetValue()
                        or self.TextBoxKPV_K5TSVedit3.GetValue() != self.TextBoxKPV_K5TSV3.GetValue()
                        or self.TextBoxKPV_K5TSVedit4.GetValue() != self.TextBoxKPV_K5TSV4.GetValue()
                        or self.TextBoxKPV_K5TSVedit5.GetValue() != self.TextBoxKPV_K5TSV5.GetValue()
                        or (self.TextBoxKPV_K5VHV1.GetValue() != "" and self.TextBoxKPV_K5VHV1.GetValue() != self.TextBoxHV_VHV.GetValue())
                        or (self.TextBoxKPV_K5VHV2.GetValue() != "" and self.TextBoxKPV_K5VHV2.GetValue() != self.TextBoxHV_VHV.GetValue())
                        or (self.TextBoxKPV_K5VHV3.GetValue() != "" and self.TextBoxKPV_K5VHV3.GetValue() != self.TextBoxHV_VHV.GetValue())
                        or (self.TextBoxKPV_K5VHV4.GetValue() != "" and self.TextBoxKPV_K5VHV4.GetValue() != self.TextBoxHV_VHV.GetValue())
                            or (self.TextBoxKPV_K5VHV5.GetValue() != "" and self.TextBoxKPV_K5VHV5.GetValue() != self.TextBoxHV_VHV.GetValue())):
                        flowables.append(
                            Paragraph("* hodnota zadaná priamo", sample_style_sheet['NormalText']))

                    flowables.append(Spacer(1, 10))

                    data = [[Paragraph("kp = k1 . k2 . k3 . k4 . k5 - koeficientu predajnosti vozidla bezprostredne pred poškodením", sample_style_sheet['TabTextLeft']),
                            Paragraph(self.TextBoxKPV_Kp.GetValue(), sample_style_sheet['TabTextRight'])],
                            [Paragraph("VŠH - výpočet všeobecnej hodnoty vozidla  = TH . kp", sample_style_sheet['TabTextLeft']),
                            Paragraph(self.TextBoxHV_VSH.GetValue() + " €", sample_style_sheet['TabTextRight'])],]

                    t = Table(data, colWidths=[my_doc.width*85/100,
                                            my_doc.width*15/100])
                    t.setStyle(TableStyle(
                        [('GRID', (0, 0), (-1, -1), 1, colors.black)]))  # (column, row)
                    flowables.append(t)

                my_doc.build(flowables)
                os.startfile(pathname)
            except IOError:
                wx.LogError(
                    "Cannot save current data in file '%s'." % pathname)
            except Exception as err:
                wx.MessageBox("Error: " + err.__str__(), "Attention",
                              wx.ICON_ERROR | wx.OK, self)

    def ButtonUlozitDOdbOnButtonClick(self, event):
        con = sqlite3.connect("vdc.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS vdc(n_id_vdc INTEGER PRIMARY KEY AUTOINCREMENT, s_cpu TEXT, s_ecv TEXT, s_data TEXT, s_date_create TEXT, s_date_last_change TEXT)")
        try:
            if self.TextBoxCisloPripadu.GetValue() == "":
                res = cur.execute("""INSERT INTO vdc(s_cpu, s_ecv, s_data, s_date_create, s_date_last_change)
                        VALUES (?, ?, ?, datetime('now', 'localtime'), datetime('now', 'localtime')) RETURNING n_id_vdc""", (self.TextBoxCPU.GetValue(), self.TextBoxECV.GetValue(), json.dumps(functionVDC.GetVDCdata(self), ensure_ascii=False)))
                self.TextBoxCisloPripadu.SetValue(str(res.fetchone()[0]))
                con.commit()
            else:
                cur.execute("""UPDATE vdc SET s_cpu = ?, s_ecv = ?, s_data = ?, s_date_last_change = datetime('now', 'localtime')
                            WHERE n_id_vdc = ?""", (self.TextBoxCPU.GetValue(), self.TextBoxECV.GetValue(), json.dumps(functionVDC.GetVDCdata(self), ensure_ascii=False), self.TextBoxCisloPripadu.GetValue()))
                con.commit()
        except Exception as err:
            wx.MessageBox("Error: " + err.__str__(), "Attention",
                              wx.ICON_ERROR | wx.OK, self)
        else:
            wx.MessageBox("Údaje uložené do databázy", "Information",
                              wx.ICON_INFORMATION | wx.OK, self)

    def ButtonOtvoritZdbOnButtonClick(self, event):
        self.child_frame = None
        VDCdbDlg(self).ShowModal()
        if self.child_frame.datavdc is not None:
            functionVDC.SetVDCdata(self, json.loads(self.child_frame.datavdc))          

    def ComboBoxKategoriaMVOnChoice(self, event):
        self.ComboBoxPodkategoriaMV.Clear()
        for x in constantVDC.kategorie:
            if (x[0][0:1] + ". " + x[1] == self.ComboBoxKategoriaMV.GetStringSelection()):
                self.ComboBoxPodkategoriaMV.Append(x[0] + ". " + x[2])
        self.ComboBoxTHRozdelitSkupiny.Clear()
        self.ComboBoxTHRozdelitSkupinyOnChoice(None)

    def ComboBoxPodkategoriaMVOnChoice(self, event):
        self.ComboBoxTHRozdelitSkupiny.Clear()
        self.ComboBoxTHRozdelitSkupiny.Append("Vozidlo ako celok")
        for x in constantVDC.skupiny:
            if (x[0][0:1] == self.ComboBoxPodkategoriaMV.GetStringSelection()[0]):
                self.ComboBoxTHRozdelitSkupiny.Append(x[1])
        self.ComboBoxTHRozdelitSkupiny.SetSelection(0)
        self.ComboBoxTHRozdelitSkupinyOnChoice(None)

        self.ComboBoxKPV_prevadzka.Clear()
        self.ComboBoxKPV_prevadzka.Append(constantVDC.pouzitiek4[1][0])
        i = 0
        for x in constantVDC.pouzitiek4[0]:
            if (x == self.ComboBoxPodkategoriaMV.GetStringSelection()[0:3]):
                break
            i += 1
        if (i < 17):
            for x in constantVDC.pouzitiek4[2:]:
                if (x[i] != ""):
                    self.ComboBoxKPV_prevadzka.Append(x[0])
        self.ComboBoxKPV_prevadzka.SetSelection(0)

    def DateTimePickerPrideleneECVOnDateChanged(self, event):
        self.TextBoxPrideleneECV.SetValue(
            self.DateTimePickerPrideleneECV.GetValue().Format("%d.%m.%Y"))
        functionVDC.PocitajDatumVprevadzkeOd(self)

    def TextBoxPrideleneECVOnKillFocus(self, event):
        if (functionVDC.KontrolujDatum(self.TextBoxPrideleneECV)):
            functionVDC.PocitajDatumVprevadzkeOd(self)
            event.Skip()

    def DateTimePickerDatumPUOnDateChanged(self, event):
        self.TextBoxDatumPU.SetValue(
            self.DateTimePickerDatumPU.GetValue().Format("%d.%m.%Y"))
        functionVDC.PocitajDatumVprevadzkeOd(self)

    def TextBoxDatumPUOnKillFocus(self, event):
        if (functionVDC.KontrolujDatum(self.TextBoxDatumPU)):
            functionVDC.PocitajDatumVprevadzkeOd(self)
            event.Skip()

    def TextBoxOdjazdeneOnKillFocus(self, event):
        if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 0)):
            functionVDC.PocitajTH(self, "TextBoxOdjazdeneOnKillFocus")
            event.Skip()

    def DateTimePickerVprevadzkeOdOnDateChanged(self, event):
        self.TextBoxVprevadzkeOd.SetValue(
            self.DateTimePickerVprevadzkeOd.GetValue().Format("%d.%m.%Y"))
        functionVDC.VypocitajDobuPrevadzky(self)

    def TextBoxVprevadzkeOdOnKillFocus(self, event):
        if (functionVDC.KontrolujDatum(self.TextBoxVprevadzkeOd)):
            functionVDC.VypocitajDobuPrevadzky(self)
            event.Skip()

    def TextBoxRokVyrobyMVOnKillFocus(self, event):
        if (functionVDC.KontrolujRokVyrobyMV(self.TextBoxRokVyrobyMV)):
            functionVDC.PocitajDatumVprevadzkeOd(self)
            event.Skip()

    def TextBoxPneuPocetOnKillFocus(self, event):
        if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 0)):
            functionVDC.PocitajTHPneu(self)
            event.Skip()

    def TextBoxPneuPriamaTHOnKillFocus(self, event):
        if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 4)):
            functionVDC.PocitajTHPneu(self)
            event.Skip()

    def TextBoxPneuMMOnKillFocus(self, event):
        if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 1)):
            functionVDC.PocitajTHPneu(self)
            event.Skip()

    def ComboBoxTHRozdelitSkupinyOnChoice(self, event):
        for i in range(1, 10):
            exec("self.TextBoxTHSkupina" + str(i) + ".SetValue('')")
            exec("self.TextBoxTHVTSS" + str(i) + ".SetValue('')")
            exec("self.TextBoxTHPDS" + str(i) + ".SetValue('')")
            exec("self.TextBoxTHZAV" + str(i) + ".SetValue('')")
            exec("self.TextBoxTHZA" + str(i) + ".SetValue('')")
            exec("self.TextBoxTHZP" + str(i) + ".SetValue('')")
            exec("self.TextBoxTHTSS" + str(i) + ".SetValue('')")
            exec("self.TextBoxTHTSS" + str(i) + "edit.SetValue('')")
            exec("self.TextBoxTHPTSS" + str(i) + ".SetValue('')")
        self.TextBoxTHTSV.SetValue('')

        if (self.ComboBoxTHRozdelitSkupiny.GetStringSelection() == "Vozidlo ako celok"):
            for x in constantVDC.kategorie:
                if (x[0][0:1] + ". " + x[1] == self.ComboBoxKategoriaMV.GetStringSelection()):
                    self.TextBoxTHSkupina1.SetValue("Vozidlo ako celok")
                    self.TextBoxTHVTSS1.SetValue("100,0000")
                    self.TextBoxTHZP1.SetValue("0,0000")
                    self.TextBoxTHPDS1.SetValue(
                        functionVDC.FormatujCisloFloatString(x[13], 4))
                    self.TextBoxTHSkupina2.SetValue("Pneumatiky")
                    self.TextBoxTHVTSS2.SetValue("100,0000")
                    self.TextBoxTHZP2.SetValue("0,0000")
                    self.TextBoxTHPDS2.SetValue(
                        functionVDC.FormatujCisloFloatString(x[14], 4))
                    break
        elif (self.ComboBoxTHRozdelitSkupiny.GetStringSelection() != ""):
            for x in constantVDC.skupiny:
                if (x[1] == self.ComboBoxTHRozdelitSkupiny.GetStringSelection()):
                    poradie = 1
                    stlpec = 2
                    for y in x[2:]:
                        if (y != ""):
                            exec("self.TextBoxTHSkupina" + str(poradie) +
                                 ".SetValue(constantVDC.skupiny[0][stlpec])")
                            exec("self.TextBoxTHVTSS" +
                                 str(poradie) + ".SetValue('100,0000')")
                            exec("self.TextBoxTHZP" +
                                 str(poradie) + ".SetValue('0,0000')")
                            exec("self.TextBoxTHPDS" + str(poradie) +
                                 ".SetValue(functionVDC.FormatujCisloFloatString(y,4))")
                            poradie += 1
                        stlpec += 1
        functionVDC.PocitajTH(self, "ComboBoxTHRozdelitSkupinyOnChoice")

    def TextBoxTHSkupinaOnKillFocus(self, event):
        if (event.GetEventObject().GetValue() == ""):
            exec("self.TextBoxTHVTSS" +
                 event.GetEventObject().GetName().split("#")[1] + ".SetValue('')")
            exec("self.TextBoxTHPDS" +
                 event.GetEventObject().GetName().split("#")[1] + ".SetValue('')")
            exec("self.TextBoxTHZAV" +
                 event.GetEventObject().GetName().split("#")[1] + ".SetValue('')")
            exec("self.TextBoxTHZA" +
                 event.GetEventObject().GetName().split("#")[1] + ".SetValue('')")
            exec("self.TextBoxTHZP" +
                 event.GetEventObject().GetName().split("#")[1] + ".SetValue('')")
            exec("self.TextBoxTHTSS" +
                 event.GetEventObject().GetName().split("#")[1] + ".SetValue('')")
            exec("self.TextBoxTHTSS" +
                 event.GetEventObject().GetName().split("#")[1] + "edit.SetValue('')")

        functionVDC.PocitajTH(self, "TextBoxTHSkupinaOnKillFocus")
        event.Skip()

    def TextBoxTHVTSSOnKillFocus(self, event):
        if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 4)):
            functionVDC.PocitajTH(self, "TextBoxTHVTSSOnKillFocus")
            event.Skip()

    def TextBoxTHPDSOnKillFocus(self, event):
        if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 4)):
            functionVDC.PocitajTH(self, "TextBoxTHPDSOnKillFocus")
            event.Skip()

    def TextBoxTHZPOnKillFocus(self, event):
        if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 4)):
            functionVDC.PocitajTH(self, "TextBoxTHZPOnKillFocus")
            event.Skip()

    def TextBoxTHTSSeditOnKillFocus(self, event):
        if (event.GetEventObject().GetValue() == ""):
            exec("event.GetEventObject().SetValue(self.TextBoxTHTSS" +
                 event.GetEventObject().GetName().split("#")[1] + ".GetValue())")
        if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 4)):
            functionVDC.PocitajTH(self, "TextBoxTHTSSeditOnKillFocus")
            event.Skip()

    def TextBoxHV_VHVOnKillFocus(self, event):
        if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 2)):
            functionVDC.PocitajVSH(self, "TextBoxHV_VHVOnKillFocus")
            event.Skip()

    def TextBoxHV_TSMVOnKillFocus(self, event):
        if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 4)):
            functionVDC.PocitajVSH(self, "TextBoxHV_TSMVOnKillFocus")
            event.Skip()

    def DatePickerTextBoxKPV_koniecTKOnDateChanged(self, event):
        self.TextBoxKPV_koniecTK.SetValue(
            self.DatePickerTextBoxKPV_koniecTK.GetValue().Format("%d.%m.%Y"))
        functionVDC.PocitajVSH(
            self, "DatePickerTextBoxKPV_koniecTKOnDateChanged")

    def TextBoxKPV_koniecTKOnKillFocus(self, event):
        if (functionVDC.KontrolujDatum(event.GetEventObject())):
            functionVDC.PocitajVSH(self, "TextBoxKPV_koniecTKOnKillFocus")
            event.Skip()

    def ComboBoxKPV_poskodenieOnChoice(self, event):
        functionVDC.PocitajVSH(self, "ComboBoxKPV_poskodenieOnChoice")

    def TextBoxKPVPocetDrzitelovOnSpinCtrl(self, event):
        functionVDC.PocitajVSH(self, "TextBoxKPVPocetDrzitelovOnSpinCtrl")

    def CheckBoxKPVk3NezisteneOnCheckBox(self, event):
        if (self.CheckBoxKPVk3Nezistene.IsChecked()):
            self.TextBoxKPVPocetDrzitelov.SetValue("")
            self.TextBoxKPVPocetDrzitelov.Disable()
        else:
            self.TextBoxKPVPocetDrzitelov.SetValue(1)
            self.TextBoxKPVPocetDrzitelov.Enable()
        functionVDC.PocitajVSH(self, "CheckBoxKPVk3NezisteneOnCheckBox")

    def ComboBoxKPV_prevadzkaOnChoice(self, event):
        i = 0
        for x in constantVDC.pouzitiek4:
            if (x[0] == self.ComboBoxKPV_prevadzka.GetStringSelection()):
                break
            i += 1
        if (constantVDC.pouzitiek4[i][16] != ""):
            self.LabelKPV_k1lehotaTKsuStazPodm.SetLabel(
                constantVDC.pouzitiek4[i][16])

        if (constantVDC.pouzitiek4[i][14] != "" and constantVDC.pouzitiek4[i][15] != ""):
            self.LabelKPV_k1a.SetLabel(constantVDC.pouzitiek4[i][14])
            self.LabelKPV_k1b.SetLabel(constantVDC.pouzitiek4[i][15])
        else:
            for x in constantVDC.kategorie:
                if (x[0][0:1] + ". " + x[1] == self.ComboBoxKategoriaMV.GetStringSelection()):
                    self.LabelKPV_k1a.SetLabel(x[15])
                    self.LabelKPV_k1b.SetLabel(x[16])
                    break
        functionVDC.PocitajVSH(self, "ComboBoxKPV_prevadzkaOnChoice")

    def TextBoxKPV_K5ZdrojOnKillFocus(self, event):
        functionVDC.PocitajVSH(self, "TextBoxKPV_K5ZdrojOnKillFocus")
        event.Skip()

    def TextBoxKPV_K5VHVOnKillFocus(self, event):
        if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 2)):
            exec('''if (self.TextBoxKPV_K5VHV''' + event.GetEventObject().GetName().split("#")[1] + '''.GetValue() == '' 
            and self.TextBoxKPV_K5Zdroj''' + event.GetEventObject().GetName().split("#")[1] + '''.GetValue() != ''):
                self.TextBoxKPV_K5VHV''' + event.GetEventObject().GetName().split("#")[1] + '''.SetValue(self.TextBoxHV_VHV.GetValue())''')
            functionVDC.PocitajVSH(self, "TextBoxKPV_K5VHVOnKillFocus")
            event.Skip()

    def TextBoxKPV_K5vPrevadzkeOnKillFocus(self, event):
        if (functionVDC.KontrolujDatum(event.GetEventObject())):
            functionVDC.PocitajVSH(self, "TextBoxKPV_K5vPrevadzkeOnKillFocus")
            event.Skip()

    def TextBoxKPV_K5kmOnKillFocus(self, event):
        if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 0)):
            functionVDC.PocitajVSH(self, "TextBoxKPV_K5kmOnKillFocus")
            event.Skip()

    def TextBoxKPV_K5CenaOnKillFocus(self, event):
        if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 2)):
            functionVDC.PocitajVSH(self, "TextBoxKPV_K5CenaOnKillFocus")
            event.Skip()

    def TextBoxKPV_K5TSVeditOnKillFocus(self, event):
        if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 4)):
            functionVDC.PocitajVSH(self, "TextBoxKPV_K5TSVeditOnKillFocus")
            event.Skip()

    def TextBoxKPV_K5VHMVOnKillFocus(self, event):
        if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 2)):
            functionVDC.PocitajVSH(self, "TextBoxKPV_K5VHMVOnKillFocus")
            event.Skip()

    def TextBoxKPV_K5TSMVOnKillFocus(self, event):
        if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 4)):
            functionVDC.PocitajVSH(self, "TextBoxKPV_K5TSMVOnKillFocus")
            event.Skip()

    def TextBoxKPV_K5OnKillFocus(self, event):
        if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 4)):
            functionVDC.PocitajVSH(self, "TextBoxKPV_K5TSMVOnKillFocus")
            event.Skip()

    def SetFocus( self, event ):
        if event.GetEventObject().GetName().split("#")[0] in constantVDC.informacia:
            self.TextBoxInformacia.SetValue(constantVDC.informacia[event.GetEventObject().GetName().split("#")[0]])
        else:
            self.TextBoxInformacia.SetValue(event.GetEventObject().GetName().split("#")[0])
        event.Skip()

    def ButtonTestOnButtonClick( self, event ):
        import openpyxl
        import re
        with wx.FileDialog(self, "Test excel file", wildcard="Test excel file (*.xlsx)|*.xlsx",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            pathname = fileDialog.GetPath()
            wrkbk = openpyxl.load_workbook(pathname)
            sh = wrkbk.active
            for i in range(2, 100):
                data = sh.cell(row=i, column=6).value
                
                dataTextBoxPoznamka = re.search(r'<TextBoxPoznamka>([\s\S]*?)</TextBoxPoznamka>', data, flags=re.MULTILINE)
                dataStr = re.sub(r'<TextBoxPoznamka>([\s\S]*?)</TextBoxPoznamka>', r'', data, flags=re.MULTILINE)
                if dataTextBoxPoznamka:
                    dataTextBoxPoznamka = dataTextBoxPoznamka.group()
                    dataTextBoxPoznamka = re.sub(r'\n', r'', dataTextBoxPoznamka)
                    dataStr = dataTextBoxPoznamka + dataStr
                dataStr = re.sub(r'^<', r'"', dataStr, flags=re.MULTILINE)
                dataStr = re.sub(r'^(.*?)>', r'\1": "', dataStr, flags=re.MULTILINE)   
                dataStr = re.sub(r'</\S*>_x000D_$', r'"', dataStr)         
                dataStr = re.sub(r'</\S*>_x000D_\n', r'", ', dataStr) 
                dataStr = re.sub(r'</\S*>\n$', r'"', dataStr)         
                dataStr = re.sub(r'</\S*>\n', r'", ', dataStr)                
                dataStr = re.sub(r'ComboBoxPlatcaDPH', r'CheckBoxPlatcaDPH', dataStr)
                dataStr = re.sub(r'"CheckBoxPlatcaDPH": "Nie"', r'"CheckBoxPlatcaDPH": false', dataStr)
                dataStr = re.sub(r'"CheckBoxPlatcaDPH": "Áno"', r'"CheckBoxPlatcaDPH": true', dataStr)
                dataStr = re.sub(r'TextBoxKPV_K5TSV1edit', r'TextBoxKPV_K5TSVedit1', dataStr)
                dataStr = re.sub(r'TextBoxKPV_K5TSV2edit', r'TextBoxKPV_K5TSVedit2', dataStr)
                dataStr = re.sub(r'TextBoxKPV_K5TSV3edit', r'TextBoxKPV_K5TSVedit3', dataStr)
                dataStr = re.sub(r'TextBoxKPV_K5TSV4edit', r'TextBoxKPV_K5TSVedit4', dataStr)
                dataStr = re.sub(r'TextBoxKPV_K5TSV5edit', r'TextBoxKPV_K5TSVedit5', dataStr)
                dataStr = re.sub(r'"CheckBoxKPVk3Nezistene": "True"', r'"CheckBoxKPVk3Nezistene": true', dataStr)
                dataStr = re.sub(r'"CheckBoxKPVk3Nezistene": "False"', r'"CheckBoxKPVk3Nezistene": false', dataStr)  
                if "TextBoxHV_VSH" in json.loads("{" + dataStr + "}"):
                    functionVDC.SetVDCdata(self, json.loads("{" + dataStr + "}"))            
                    print(i, json.loads("{" + dataStr + "}")["TextBoxHV_VSH"], self.TextBoxHV_VSH.GetValue(), "OK" if json.loads("{" + dataStr + "}")["TextBoxHV_VSH"] == self.TextBoxHV_VSH.GetValue() else "WRONG" )   

class VDCdbDlg(formVDCmain.VDCdb):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        formVDCmain.VDCdb.__init__(self, parent)
        self.GridVysledkyVyhladavania.SetSelectionMode(wx.grid.Grid.GridSelectRows)
        parent.child_frame = self
        self.datavdc = None

    def ButtonVyhladatOnButtonClick( self, event ):
        if self.GridVysledkyVyhladavania.GetNumberRows() > 0:
            self.GridVysledkyVyhladavania.DeleteRows(0, self.GridVysledkyVyhladavania.GetNumberRows())
        con = sqlite3.connect("vdc.db")
        cur = con.cursor()
        sqlquery = "SELECT _rowid_, n_id_vdc, s_cpu, s_ecv, s_date_create, s_date_last_change FROM vdc WHERE 1=1"
        if self.TextBoxVyhladavanieID.GetValue() != "":
            sqlquery += " AND n_id_vdc = " + self.TextBoxVyhladavanieID.GetValue()
        if self.TextBoxVyhladavanieCisloPU.GetValue() != "":
            sqlquery += " AND s_cpu LIKE '" + self.TextBoxVyhladavanieCisloPU.GetValue() + "'"
        if self.TextBoxVyhladavanieECV.GetValue() != "":
            sqlquery += " AND s_ecv LIKE '" + self.TextBoxVyhladavanieECV.GetValue() + "'"

        try:                   
            res = cur.execute(sqlquery)
            datavdc = res.fetchall()

            for row in datavdc:
                self.GridVysledkyVyhladavania.AppendRows(1)
                self.GridVysledkyVyhladavania.SetCellValue(row[0] - 1, 0, str(row[1]))
                self.GridVysledkyVyhladavania.SetCellValue(row[0] - 1, 1, str(row[2]))
                self.GridVysledkyVyhladavania.SetCellValue(row[0] - 1, 2, str(row[3]))
                self.GridVysledkyVyhladavania.SetCellValue(row[0] - 1, 3, str(row[4]))
                self.GridVysledkyVyhladavania.SetCellValue(row[0] - 1, 4, str(row[5]))
        except Exception as err:
            wx.MessageBox("Error: " + err.__str__(), "Attention",
                              wx.ICON_ERROR | wx.OK, self)

    def ButtonZobrazitOnButtonClick( self, event ):
        if self.GridVysledkyVyhladavania.GetSelectedRows():
            con = sqlite3.connect("vdc.db")
            cur = con.cursor()
            try:                   
                res = cur.execute("SELECT s_data FROm vdc WHERE n_id_vdc = ?", self.GridVysledkyVyhladavania.GetCellValue(self.GridVysledkyVyhladavania.GetSelectedRows()[0],0))
                self.datavdc = res.fetchone()[0]
                self.Close()

            except Exception as err:
                wx.MessageBox("Error: " + err.__str__(), "Attention",
                              wx.ICON_ERROR | wx.OK, self)

    def ButtonNoveVyhladavanieOnButtonClick( self, event ):
        if self.GridVysledkyVyhladavania.GetNumberRows() > 0:
            self.GridVysledkyVyhladavania.DeleteRows(0, self.GridVysledkyVyhladavania.GetNumberRows())
        self.TextBoxVyhladavanieCisloPU.SetValue("")
        self.TextBoxVyhladavanieECV.SetValue("")
        self.TextBoxVyhladavanieID.SetValue("")

# mandatory in wx, create an app
app = wx.App(False)
app.ResetLocale()  # aby fungovalo datetime.strptime

# create an object of CalcFrame
frame = VDCFrame(None)

if (os.path.isfile("Car.ico")):
    frame.SetIcon(wx.Icon("Car.ico", wx.BITMAP_TYPE_ICO))
if (os.path.isfile("VDC.exe")):
    frame.SetIcon(wx.Icon("VDC.exe", wx.BITMAP_TYPE_ICO))

# show the frame
frame.Show(True)

# start the applications
app.MainLoop()


# Ternary Operator in Python Syntax : [on_true] if [expression] else [on_false]
