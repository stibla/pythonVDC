from datetime import datetime
from datetime import date
import wx

import constantVDC

def KontrolujDatum(control):
    if (len(control.GetValue()) == 0):
        return True
    try:
        control.SetValue(
            (datetime.strptime(control.GetValue(), "%d.%m.%Y")).strftime("%d.%m.%Y"))
        return True
    except ValueError:
        wx.MessageBox(
            'Nekorektný dátum. Zadajte v tvare DD.MM.RRRR', 'Upozornenie', wx.OK)
        control.SetFocus()
        control.SelectAll()
        return False


def KontrolujRokVyrobyMV(control):
    if (len(control.GetValue()) == 0):
        return True
    if (control.GetValue().isnumeric()):
        if (int(control.GetValue()) >= 1900 and int(control.GetValue()) <= date.today().year):
            control.SetValue(str(int(control.GetValue())))
            return True
    wx.MessageBox(
        'Nekorektne zadaný rok výroby. Musí byť v intervale 1900 - ' + str(date.today().year), 'Upozornenie', wx.OK)
    control.SetFocus()
    control.SelectAll()
    return False


def KontrolujFloatCislo(control, noOfDecimal):
    if (len(control.GetValue()) == 0):
        return True
    try:
        control.SetValue(str("{0:,."+str(noOfDecimal)+"f}").format(float(control.GetValue(
        ).replace(" ", "").replace(",", "."))).replace(",", " ").replace(".", ","))
        return True
    except ValueError:
        wx.MessageBox('Nekorektne zadaná hodnota', 'Upozornenie', wx.OK)
        control.SetFocus()
        control.SelectAll()
        return False


def JeFloat(cisloString):
    if (len(cisloString) == 0):
        return True
    try:
        float(cisloString.replace(" ", "").replace(",", "."))
        return True
    except ValueError:
        return False


def FormatujCisloFloatString(cisloString, noOfDecimal):
    if (len(cisloString) == 0):
        return ""
    try:
        return str("{0:,."+str(noOfDecimal)+"f}").format(float(cisloString.replace(",", "."))).replace(",", " ").replace(".", ",")
    except ValueError:
        return ""


def FormatujCisloFloat(cisloFloat, noOfDecimal):
    try:
        return str("{0:,."+str(noOfDecimal)+"f}").format(cisloFloat).replace(",", " ").replace(".", ",")
    except ValueError:
        return ""


def StringToFloat(cisloFloat):
    return float(cisloFloat.replace(" ", "").replace(",", "."))


def rozdielDatumovVmesiacoch(odDatumString, doDatumString):
    odDatum = datetime.strptime(odDatumString, "%d.%m.%Y")
    doDatum = datetime.strptime(doDatumString, "%d.%m.%Y")    
    return (doDatum.year*12 + doDatum.month + doDatum.day / 31) - (odDatum.year*12 + odDatum.month + odDatum.day / 31)


def PocitajDatumVprevadzkeOd(parent):
    if(parent.TextBoxRokVyrobyMV.GetValue() != ""):
        parent.TextBoxVprevadzkeOd.SetValue(
            "01.07." + parent.TextBoxRokVyrobyMV.GetValue())
        if(parent.TextBoxDatumPU.GetValue() != ""):
            if(datetime.strptime(parent.TextBoxDatumPU.GetValue(), "%d.%m.%Y").year <= int(parent.TextBoxRokVyrobyMV.GetValue())):
                parent.TextBoxVprevadzkeOd.SetValue(
                    "01.01." + parent.TextBoxRokVyrobyMV.GetValue())
            elif(parent.TextBoxPrideleneECV.GetValue() != ""):
                if(datetime.strptime(parent.TextBoxPrideleneECV.GetValue(), "%d.%m.%Y").year > int(parent.TextBoxRokVyrobyMV.GetValue())):
                    parent.TextBoxVprevadzkeOd.SetValue(
                        "01.01." + str(int(parent.TextBoxRokVyrobyMV.GetValue()) + 1))
    VypocitajDobuPrevadzky(parent)


def VypocitajDobuPrevadzky(parent):
    if (parent.TextBoxDatumPU.GetValue() == ""):
        parent.TextBoxDatumPU.SetBackgroundColour((255, 192, 192, 255))
        parent.TextBoxDatumPU.Refresh()
    else:
        parent.TextBoxDatumPU.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        parent.TextBoxDatumPU.Refresh()

    if (parent.TextBoxVprevadzkeOd.GetValue() == ""):
        parent.TextBoxVprevadzkeOd.SetBackgroundColour(
            (255, 192, 192, 255))
        parent.TextBoxVprevadzkeOd.Refresh()
    else:
        parent.TextBoxVprevadzkeOd.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        parent.TextBoxVprevadzkeOd.Refresh()
    
    parent.TextBoxDobaPrevadzkyMesiac.SetValue("")
    if(parent.TextBoxDatumPU.GetValue() != "" and parent.TextBoxVprevadzkeOd.GetValue() != ""):
        if(rozdielDatumovVmesiacoch(parent.TextBoxVprevadzkeOd.GetValue(), parent.TextBoxDatumPU.GetValue()) < 0):
            wx.MessageBox(
        'Nekorektne zadaný dátum v prevádzke od alebo dátum hodnotenia ', 'Upozornenie', wx.OK)
        else:
            parent.TextBoxDobaPrevadzkyMesiac.SetValue(FormatujCisloFloat(rozdielDatumovVmesiacoch(parent.TextBoxVprevadzkeOd.GetValue(), parent.TextBoxDatumPU.GetValue()),4))
    #try:
        #datumPU = datetime.strptime(
        #    parent.TextBoxDatumPU.GetValue(), "%d.%m.%Y")
        #vPrevadzkeOd = datetime.strptime(
        #    parent.TextBoxVprevadzkeOd.GetValue(), "%d.%m.%Y")
        #parent.TextBoxDobaPrevadzkyMesiac.SetValue(FormatujCisloFloat((datumPU.year*12 + datumPU.month + datumPU.day / 31) - (
        #    vPrevadzkeOd.year*12 + vPrevadzkeOd.month + vPrevadzkeOd.day / 31), 4))
        
    #except ValueError:
        

    parent.TextBoxTHdobaPrevadzky.SetValue(
        parent.TextBoxDobaPrevadzkyMesiac.GetValue())
    PocitajTH(parent, "VypocitajDobuPrevadzky")


def PocitajTHPneu(parent):
    PocitajTHPneuJedna(parent.TextBoxPneuPocet1, parent.TextBoxPneuPriamaTH1, parent.TextBoxPneuNamerane1,
                                    parent.TextBoxPneuNove1, parent.TextBoxPneuTH1)
    PocitajTHPneuJedna(parent.TextBoxPneuPocet2, parent.TextBoxPneuPriamaTH2, parent.TextBoxPneuNamerane2,
                                    parent.TextBoxPneuNove2, parent.TextBoxPneuTH2)
    PocitajTHPneuJedna(parent.TextBoxPneuPocet3, parent.TextBoxPneuPriamaTH3, parent.TextBoxPneuNamerane3,
                                    parent.TextBoxPneuNove3, parent.TextBoxPneuTH3)

    tmpPocetPneu = 0 if parent.TextBoxPneuTH1.GetValue() == "" or parent.TextBoxPneuPocet1.GetValue(
    ) == "" else int(parent.TextBoxPneuPocet1.GetValue())
    tmpPocetPneu += 0 if parent.TextBoxPneuTH2.GetValue() == "" or parent.TextBoxPneuPocet2.GetValue(
    ) == "" else int(parent.TextBoxPneuPocet2.GetValue())
    tmpPocetPneu += 0 if parent.TextBoxPneuTH3.GetValue() == "" or parent.TextBoxPneuPocet3.GetValue(
    ) == "" else int(parent.TextBoxPneuPocet3.GetValue())

    tempTHPneu = 0 if parent.TextBoxPneuTH1.GetValue() == "" or parent.TextBoxPneuPocet1.GetValue() == "" else StringToFloat(
        parent.TextBoxPneuTH1.GetValue()) * int(parent.TextBoxPneuPocet1.GetValue())
    tempTHPneu += 0 if parent.TextBoxPneuTH2.GetValue() == "" or parent.TextBoxPneuPocet2.GetValue() == "" else StringToFloat(
        parent.TextBoxPneuTH2.GetValue()) * int(parent.TextBoxPneuPocet2.GetValue())
    tempTHPneu += 0 if parent.TextBoxPneuTH3.GetValue() == "" or parent.TextBoxPneuPocet3.GetValue() == "" else StringToFloat(
        parent.TextBoxPneuTH3.GetValue()) * int(parent.TextBoxPneuPocet3.GetValue())

    parent.TextBoxPneuTH.SetValue("")
    if (tempTHPneu != 0):
        parent.TextBoxPneuTH.SetValue(
            FormatujCisloFloat(tempTHPneu/tmpPocetPneu, 4))

    PocitajTH(parent, "PocitajTHPneu")


def PocitajTHPneuJedna(conPocet, conPriamaTH, conNamerane, conNove, conTH):
    conPocet.SetBackgroundColour(
        wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
    conPocet.Refresh()
    conPriamaTH.SetBackgroundColour(
        wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
    conPriamaTH.Refresh()
    conNamerane.SetBackgroundColour(
        wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
    conNamerane.Refresh()
    conNove.SetBackgroundColour(
        wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
    conNove.Refresh()

    if (conNamerane.GetValue() != "" and conNove.GetValue() != "" and conPriamaTH.GetValue() != ""):
        conPriamaTH.SetValue("")

    if (conPocet.GetValue() != "" or conPriamaTH.GetValue() != "" or conNamerane.GetValue() != "" or conNove.GetValue() != ""):
        if (conPocet.GetValue() == ""):
            conPocet.SetBackgroundColour((255, 192, 192, 255))
            conPocet.Refresh()
        if (conPriamaTH.GetValue() == "" and conNamerane.GetValue() == "" and conNove.GetValue() == ""):
            conPriamaTH.SetBackgroundColour((255, 192, 192, 255))
            conPriamaTH.Refresh()
            conNamerane.SetBackgroundColour((255, 192, 192, 255))
            conNamerane.Refresh()
            conNove.SetBackgroundColour((255, 192, 192, 255))
            conNove.Refresh()
        if (conNamerane.GetValue() == "" and conNove.GetValue() != ""):
            conNamerane.SetBackgroundColour((255, 192, 192, 255))
            conNamerane.Refresh()
        if (conNamerane.GetValue() != "" and conNove.GetValue() == ""):
            conNove.SetBackgroundColour((255, 192, 192, 255))
            conNove.Refresh()

    conTH.SetValue("")
    if (conNamerane.GetValue() != "" and conNove.GetValue() != "" and conPocet.GetValue() != ""):
        try:
            conTH.SetValue(FormatujCisloFloat(StringToFloat(
                conNamerane.GetValue())/StringToFloat(conNove.GetValue())*100, 4))
        except ZeroDivisionError:
            pass

    if (conPriamaTH.GetValue() != "" and conPocet.GetValue() != ""):
        try:
            conTH.SetValue(conPriamaTH.GetValue())
        except ZeroDivisionError:
            pass


def PocitajTH(parent, ktoVola):
    print("pocitaj TH ", ktoVola)
    parent.TextBoxTHkKM.SetValue("")
    parent.TextBoxTHPKV.SetValue("")
    parent.TextBoxTHPZTS.SetValue("")
    parent.TextBoxTHPEZ.SetValue("")
    parent.LabelTHZAVa.SetLabel("")
    parent.LabelTHZAVb.SetLabel("")
    parent.LabelTHZAVc.SetLabel("")
    parent.LabelTHZAVd.SetLabel("")
    parent.LabelKPV_k1a.SetLabel("")
    parent.LabelKPV_k1b.SetLabel("")
    parent.LabelKPV_k1lehotaTK.SetLabel("")
    parent.LabelKPV_k1lehotaTKstazPodm.SetLabel("")
    for x in constantVDC.kategorie:
        if (x[0] + ". " + x[2] == parent.ComboBoxPodkategoriaMV.GetStringSelection()):
            parent.TextBoxTHkKM.SetValue(
                FormatujCisloFloatString(x[5], 4))
            parent.TextBoxTHPKV.SetValue(
                FormatujCisloFloatString(x[6], 0))
            parent.TextBoxTHPZTS.SetValue(
                FormatujCisloFloatString(x[7], 0))
            parent.TextBoxTHPEZ.SetValue(
                FormatujCisloFloatString(x[8], 0))
            parent.LabelTHZAVa.SetLabel(x[9])
            parent.LabelTHZAVb.SetLabel(x[10])
            parent.LabelTHZAVc.SetLabel(x[11])
            parent.LabelTHZAVd.SetLabel(x[12])
            parent.LabelKPV_k1a.SetLabel(x[15]) 
            parent.LabelKPV_k1b.SetLabel(x[16])
            parent.LabelKPV_k1lehotaTK.SetLabel(x[17])
            parent.LabelKPV_k1lehotaTKstazPodm.SetLabel(x[18])
            break
    parent.TextBoxTHPRKM.SetValue("")
    if(parent.TextBoxTHPKV.GetValue() != "" and parent.TextBoxTHdobaPrevadzky.GetValue() != ""):
        parent.TextBoxTHPRKM.SetValue(FormatujCisloFloat(StringToFloat(
            parent.TextBoxTHPKV.GetValue()) * StringToFloat(parent.TextBoxTHdobaPrevadzky.GetValue()) / 12, 0))
        if (StringToFloat(parent.TextBoxTHPRKM.GetValue()) > StringToFloat(parent.TextBoxTHPKV.GetValue()) * StringToFloat(parent.TextBoxTHPEZ.GetValue())):
            parent.TextBoxTHPRKM.SetValue(FormatujCisloFloat(StringToFloat(
                parent.TextBoxTHPKV.GetValue()) * StringToFloat(parent.TextBoxTHPEZ.GetValue()), 0))

    parent.TextBoxOdjazdene.SetBackgroundColour(
        wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
    if (parent.TextBoxOdjazdene.GetValue() == ""):
        parent.TextBoxOdjazdene.SetBackgroundColour((255, 192, 192, 255))
    parent.TextBoxOdjazdene.Refresh()

    parent.TextBoxTHRKM.SetValue("")
    if(parent.TextBoxTHPRKM.GetValue() != "" and parent.TextBoxOdjazdene.GetValue() != ""):
        parent.TextBoxTHRKM.SetValue(FormatujCisloFloat(StringToFloat(
            parent.TextBoxOdjazdene.GetValue()) - StringToFloat(parent.TextBoxTHPRKM.GetValue()), 2))

    parent.TextBoxTHkAM.SetValue("")
    if(parent.TextBoxTHRKM.GetValue() != "" and parent.TextBoxTHkKM.GetValue() != ""):
        parent.TextBoxTHkAM.SetValue(FormatujCisloFloat(StringToFloat(
            parent.TextBoxTHRKM.GetValue()) * StringToFloat(parent.TextBoxTHkKM.GetValue()) / 1000, 4))

    parent.TextBoxTHPDSSpolu.SetValue("")

    globals()['temp'] = 0
    for i in range(1, 10):
        exec("if (parent.TextBoxTHPDS" + str(i) + ".GetValue() != '' and JeFloat(parent.TextBoxTHPDS" + str(i) +
                ".GetValue())): globals()['temp'] += StringToFloat(parent.TextBoxTHPDS" + str(i) + ".GetValue())")
    
    parent.TextBoxTHPDSSpolu.SetValue(
        FormatujCisloFloat(globals()['temp'], 4))
    if (parent.TextBoxTHPDSSpolu.GetValue() != "100,0000"):
        parent.TextBoxTHPDSSpolu.SetBackgroundColour((255, 192, 192, 255))
    else:
        parent.TextBoxTHPDSSpolu.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
    parent.TextBoxTHPDSSpolu.Refresh()
    
    globals()['temp'] = 0
    for i in range(1, 10):
        exec('''parent.TextBoxTHZAV''' + str(i) + '''.SetValue("") 
parent.TextBoxTHZA''' + str(i) + '''.SetValue("")
tempTextBoxTHTSS = parent.TextBoxTHTSS''' + str(i) + '''.GetValue()
parent.TextBoxTHTSS''' + str(i) + '''.SetValue("")
parent.TextBoxTHPTSS''' + str(i) + '''.SetValue("")

if (parent.TextBoxTHSkupina''' + str(i) + '''.GetValue() != "" and parent.TextBoxTHdobaPrevadzky.GetValue() != ""):
        if (parent.TextBoxTHZP''' + str(i) + '''.GetValue() == ""):
            parent.TextBoxTHZP''' + str(i) + '''.SetValue("0,0000")

        if (parent.TextBoxTHSkupina''' + str(i) + '''.GetValue() != "Pneumatiky"):
            if (parent.LabelTHZAVd.GetLabel() == ""):
                parent.TextBoxTHZAV''' + str(i) + '''.SetValue(FormatujCisloFloat(StringToFloat(parent.LabelTHZAVa.GetLabel()) +
                                                                            ((StringToFloat(parent.TextBoxTHdobaPrevadzky.GetValue()) +
                                                                            StringToFloat(parent.LabelTHZAVb.GetLabel())) /
                                                                            StringToFloat(parent.LabelTHZAVc.GetLabel())) ** (1/2), 4))
            else:
                parent.TextBoxTHZAV''' + str(i) + '''.SetValue(FormatujCisloFloat(StringToFloat(parent.LabelTHZAVd.GetLabel()) *
                                                                            StringToFloat(parent.TextBoxTHdobaPrevadzky.GetValue()), 4))

            if (StringToFloat(parent.TextBoxTHZAV''' + str(i) + '''.GetValue()) > 100 - StringToFloat(parent.TextBoxTHPZTS.GetValue())):
                parent.TextBoxTHZAV''' + str(i) + '''.SetValue(FormatujCisloFloat(
                    100 - StringToFloat(parent.TextBoxTHPZTS.GetValue()), 4))
            
            if (parent.TextBoxTHkAM.GetValue() != ""):
                parent.TextBoxTHZA''' + str(i) + '''.SetValue(FormatujCisloFloat((StringToFloat(parent.TextBoxTHVTSS''' + str(i) + '''.GetValue()) -
                                                                            StringToFloat(parent.TextBoxTHVTSS''' + str(i) + '''.GetValue()) / 100 *
                                                                            StringToFloat(parent.TextBoxTHZAV''' + str(i) + '''.GetValue())) *
                                                                            (StringToFloat(parent.TextBoxTHkAM.GetValue()) / 100) + 
                                                                            StringToFloat(parent.TextBoxTHZAV''' + str(i) + '''.GetValue()) , 4))
            else:
                parent.TextBoxTHZA''' + str(i) + '''.SetValue(FormatujCisloFloat(StringToFloat(parent.TextBoxTHZAV''' + str(i) + '''.GetValue()) , 4))                                                                            
            
            parent.TextBoxTHTSS''' + str(i) + '''.SetValue(FormatujCisloFloat(((StringToFloat(parent.TextBoxTHVTSS''' + str(i) + '''.GetValue()) *
                                                                        (100 - StringToFloat(parent.TextBoxTHZA''' + str(i) + '''.GetValue())))  *
                                                                        (100 + StringToFloat(parent.TextBoxTHZP''' + str(i) + '''.GetValue()))) / 10000 , 4))
        else:
            if (parent.TextBoxPneuTH.GetValue() != ""):
                parent.TextBoxTHTSS''' + str(i) + '''.SetValue(FormatujCisloFloat(StringToFloat(parent.TextBoxPneuTH.GetValue()), 4))  
            else:
                parent.TextBoxTHTSS''' + str(i) + '''.SetValue("0,0000")
            parent.TextBoxTHVTSS''' + str(i) + '''.SetValue("")
            parent.TextBoxTHZP''' + str(i) + '''.SetValue("")

        if (parent.TextBoxTHTSS''' + str(i) + '''edit.GetValue() == "" or tempTextBoxTHTSS != parent.TextBoxTHTSS''' + str(i) + '''.GetValue()):
            parent.TextBoxTHTSS''' + str(i) + '''edit.SetValue(parent.TextBoxTHTSS''' + str(i) + '''.GetValue())

        parent.TextBoxTHPTSS''' + str(i) + '''.SetValue(FormatujCisloFloat(StringToFloat(parent.TextBoxTHTSS''' + str(i) + '''edit.GetValue()) *
                                                                    StringToFloat(parent.TextBoxTHPDS''' + str(i) + '''.GetValue()) / 100 , 4))

        if (parent.TextBoxTHTSS''' + str(i) + '''edit.GetValue() != parent.TextBoxTHTSS''' + str(i) + '''.GetValue()):
            parent.TextBoxTHZAV''' + str(i) + '''.SetValue("-          ")
            parent.TextBoxTHZA''' + str(i) + '''.SetValue("-          ")
            parent.TextBoxTHZP''' + str(i) + '''.SetValue("")

        if(parent.TextBoxTHPTSS''' + str(i) + '''.GetValue() != ""):
            globals()['temp'] += StringToFloat(parent.TextBoxTHPTSS''' + str(i) + '''.GetValue())
        ''')
    
    parent.TextBoxTHTSV.SetValue("")
    if (globals()['temp'] != 0 and parent.TextBoxTHPDSSpolu.GetValue() == "100,0000"):
        if (parent.TextBoxTHPZTS.GetValue() != ""):
            if (globals()['temp'] < StringToFloat(parent.TextBoxTHPZTS.GetValue())):
                globals()['temp'] = StringToFloat(parent.TextBoxTHPZTS.GetValue())
        parent.TextBoxTHTSV.SetValue(FormatujCisloFloat(globals()['temp'], 4))
    parent.TextBoxHV_TSV.SetValue(parent.TextBoxTHTSV.GetValue())

    PocitajVSH(parent, "PocitajTH")

def PocitajVSH(parent, ktoVola):
    print("pocitaj VSH ", ktoVola)
    parent.TextBoxHV_TH.SetValue("")
    if(parent.TextBoxHV_VHV.GetValue() != "" and parent.TextBoxHV_TSV.GetValue() != ""):
        if(parent.TextBoxHV_VHMV.GetValue() != "" and parent.TextBoxHV_TSMV.GetValue() != ""):
            parent.TextBoxHV_TH.SetValue(FormatujCisloFloat(StringToFloat(parent.TextBoxHV_VHV.GetValue()) * 
            StringToFloat(parent.TextBoxHV_TSV.GetValue()) / 100 + StringToFloat(parent.TextBoxHV_VHMV.GetValue()) * 
            StringToFloat(parent.TextBoxHV_TSMV.GetValue()) / 100, 2))
            pass
        else:
            parent.TextBoxHV_TH.SetValue(FormatujCisloFloat(StringToFloat(parent.TextBoxHV_VHV.GetValue()) * 
            StringToFloat(parent.TextBoxHV_TSV.GetValue()) / 100, 2))
            pass


    parent.TextBoxKPV_K1.SetValue("1,0000")
    if (parent.TextBoxDatumPU.GetValue() != "" and parent.TextBoxKPV_koniecTK.GetValue() != "" and parent.TextBoxVprevadzkeOd.GetValue() != ""):
        if (parent.LabelKPV_k1lehotaTKsuStazPodm.GetLabel() != "1"): tempLehota = StringToFloat(parent.LabelKPV_k1lehotaTKstazPodm.GetLabel()) 
        else: tempLehota = StringToFloat(parent.LabelKPV_k1lehotaTK.GetLabel()) 
        if (tempLehota != 0 and tempLehota * 12 < StringToFloat(parent.TextBoxDobaPrevadzkyMesiac.GetValue())):
            if (parent.LabelKPV_k1a.GetLabel() != "" and parent.LabelKPV_k1b.GetLabel() != ""):               
                parent.TextBoxKPV_K1.SetValue(FormatujCisloFloat(StringToFloat(parent.LabelKPV_k1a.GetLabel()) + StringToFloat(parent.LabelKPV_k1b.GetLabel()) * rozdielDatumovVmesiacoch(parent.TextBoxDatumPU.GetValue(), parent.TextBoxKPV_koniecTK.GetValue()), 4))
            if (StringToFloat(parent.LabelKPV_k1a.GetLabel()) > StringToFloat(parent.TextBoxKPV_K1.GetValue())):
                parent.TextBoxKPV_K1.SetValue(FormatujCisloFloat(StringToFloat(parent.LabelKPV_k1a.GetLabel()), 4))

    
    parent.TextBoxKPV_K2.SetValue("1,0000")
    if (parent.ComboBoxKPV_poskodenie.GetStringSelection() != "" and parent.TextBoxDobaPrevadzkyMesiac.GetValue() != ""):
        for x in constantVDC.poskodeniek2:
            if (x[0] == parent.ComboBoxKPV_poskodenie.GetStringSelection()):                
                for i in range(1, len(constantVDC.poskodeniek2[0])):                                        
                    if(StringToFloat(parent.TextBoxDobaPrevadzkyMesiac.GetValue()) / 12 >= StringToFloat(constantVDC.poskodeniek2[0][i]) and StringToFloat(parent.TextBoxDobaPrevadzkyMesiac.GetValue()) / 12 < StringToFloat(constantVDC.poskodeniek2[0][i+1])):
                        parent.TextBoxKPV_K2.SetValue(FormatujCisloFloat(StringToFloat(x[i]), 4))
                        break
                    
    parent.TextBoxKPV_K3.SetValue("0,9500")
    if(parent.TextBoxKPVPocetDrzitelov.GetValue() != "" and not parent.CheckBoxKPVk3Nezistene.IsChecked()):
        print("parent.TextBoxKPVPocetDrzitelov.GetValue() ", parent.TextBoxKPVPocetDrzitelov.GetValue())
        parent.TextBoxKPV_K3.SetValue(FormatujCisloFloat(1.01 - 0.01 * (parent.TextBoxKPVPocetDrzitelov.GetValue()), 4))

    #     TextBoxKPV_K4.Text = "1,0000"
    #     If ComboBoxKPV_prevadzka.Text <> "" And ComboBoxPodkategoriaMV.Text <> "" Then
    #         Dim N As Long = 2
    #         Do While N <= ConstantVDC.pouzitiek4.GetUpperBound(0)
    #             If ComboBoxKPV_prevadzka.Text = ConstantVDC.pouzitiek4(N, 0) Then
    #                 Dim M As Long = 1
    #                 Do While M <= ConstantVDC.pouzitiek4.GetUpperBound(1)
    #                     If ConstantVDC.pouzitiek4(0, M) = Mid(ComboBoxPodkategoriaMV.Text, 1, 3) Then
    #                         TextBoxKPV_K4.Text = FormatDoubleMoje(CDblMoje(ConstantVDC.pouzitiek4(N, M)), "0.0000")
    #                     End If
    #                     M = M + 1
    #                 Loop
    #             End If
    #             N = N + 1
    #         Loop
    #     End If
    # pass

    # for x in constantVDC.kategorie:
    #         if (x[0] + ". " + x[2] == parent.ComboBoxPodkategoriaMV.GetStringSelection()):
    #             parent.TextBoxTHkKM.SetValue(
    #                 FormatujCisloFloatString(x[5], 4))
    #             
    #             break