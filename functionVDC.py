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
        parent.TextBoxKPV_K3.SetValue(FormatujCisloFloat(1.01 - 0.01 * (parent.TextBoxKPVPocetDrzitelov.GetValue()), 4))

    parent.TextBoxKPV_K4.SetValue("1,0000")
    if (parent.ComboBoxKPV_prevadzka.GetStringSelection() != "" and parent.ComboBoxPodkategoriaMV.GetStringSelection() != ""):
        for x in constantVDC.pouzitiek4:
            if (x[0] == parent.ComboBoxKPV_prevadzka.GetStringSelection()):                
                for i in range(1, len(constantVDC.pouzitiek4[0])):
                    if (constantVDC.pouzitiek4[0][i] == parent.ComboBoxPodkategoriaMV.GetStringSelection()[0:3]):
                        parent.TextBoxKPV_K4.SetValue(FormatujCisloFloat(StringToFloat(x[i]), 4))
                        break


    #    PocitajTSV(TextBoxKPV_K5vPrevadzke1, TextBoxKPV_K5km1, TextBoxKPV_K5TSV1, TextBoxKPV_K5TSV1edit)
    # Sub PocitajTSV(TBKPV_K5vPrevadzke As Windows.Forms.TextBox, KPV_K5km As Windows.Forms.TextBox, TBKPV_K5TSV As Windows.Forms.TextBox, TextBoxKPV_K5TSVedit As Windows.Forms.TextBox)
    #     Dim tempTHZAV, tempTHZA, tempDobaPrevadzkyMesiac, tempTHPRKM As Double
    #     Dim tempOldTBKPV_K5TSV As String
    #     tempTHZAV = 0
    #     tempTHZA = 0
    #     tempDobaPrevadzkyMesiac = 0
    #     tempTHPRKM = 0
    #     tempOldTBKPV_K5TSV = TBKPV_K5TSV.Text
    #     TBKPV_K5TSV.Text = ""
    #     If TextBoxTHPZTS.Text <> "" And KPV_K5km.Text <> "" And TextBoxDatumPU.Text <> "" And TBKPV_K5vPrevadzke.Text <> "" Then
    #         tempDobaPrevadzkyMesiac = Math.Round((Year(DateValueMoje(TextBoxDatumPU.Text)) * 12 + Month(DateValueMoje(TextBoxDatumPU.Text)) + (Microsoft.VisualBasic.DateAndTime.Day(DateValueMoje(TextBoxDatumPU.Text)) / 31)) - (Year(DateValueMoje(TBKPV_K5vPrevadzke.Text)) * 12 + Month(DateValueMoje(TBKPV_K5vPrevadzke.Text)) + (Microsoft.VisualBasic.DateAndTime.Day(DateValueMoje(TBKPV_K5vPrevadzke.Text)) / 31)), 4)

    #         If LabelTHZAVd.Text = "" Then
    #             tempTHZAV = Math.Round(CDblMoje(LabelTHZAVa.Text) + ((tempDobaPrevadzkyMesiac + CDblMoje(LabelTHZAVb.Text)) / CDblMoje(LabelTHZAVc.Text)) ^ 0.5, 4)
    #         Else
    #             tempTHZAV = Math.Round(CDblMoje(LabelTHZAVd.Text) * tempDobaPrevadzkyMesiac, 4)
    #         End If
    #         If CDblMoje(tempTHZAV) > 100 - CDblMoje(TextBoxTHPZTS.Text) Then tempTHZAV = 100 - CDblMoje(TextBoxTHPZTS.Text)

    #         If TextBoxTHkKM.Text <> "" And TextBoxTHPKV.Text <> "" Then
    #             tempTHPRKM = Math.Round((CDblMoje(TextBoxTHPKV.Text) * tempDobaPrevadzkyMesiac / 12), 4)
    #             If tempTHPRKM > CDblMoje(TextBoxTHPKV.Text) * CDblMoje(TextBoxTHPEZ.Text) Then tempTHPRKM = Math.Round(CDblMoje(TextBoxTHPKV.Text) * CDblMoje(TextBoxTHPEZ.Text), 4)
    #             tempTHZA = Math.Round((100 - (tempTHZAV)) * (((CDblMoje(KPV_K5km.Text) - tempTHPRKM) * CDblMoje(TextBoxTHkKM.Text) / 1000) / 100) + (tempTHZAV), 4)
    #         Else
    #             tempTHZA = tempTHZAV
    #         End If

    #         If CDblMoje(TextBoxTHPZTS.Text) > ((100 * (100 - CDblMoje(tempTHZA)))) / 100 Then
    #             TBKPV_K5TSV.Text = FormatDoubleMoje(TextBoxTHPZTS.Text, "0.0000")
    #         Else
    #             TBKPV_K5TSV.Text = FormatDoubleMoje(((100 * (100 - CDblMoje(tempTHZA)))) / 100, "0.0000")
    #         End If

    #     End If
    #     If TextBoxKPV_K5TSVedit.Text = "" Or tempOldTBKPV_K5TSV <> TBKPV_K5TSV.Text Then
    #         TextBoxKPV_K5TSVedit.Text = TBKPV_K5TSV.Text
    #     End If

    # End Sub
    #     PocitajTSV(TextBoxKPV_K5vPrevadzke2, TextBoxKPV_K5km2, TextBoxKPV_K5TSV2, TextBoxKPV_K5TSV2edit)
    #     PocitajTSV(TextBoxKPV_K5vPrevadzke3, TextBoxKPV_K5km3, TextBoxKPV_K5TSV3, TextBoxKPV_K5TSV3edit)
    #     PocitajTSV(TextBoxKPV_K5vPrevadzke4, TextBoxKPV_K5km4, TextBoxKPV_K5TSV4, TextBoxKPV_K5TSV4edit)
    #     PocitajTSV(TextBoxKPV_K5vPrevadzke5, TextBoxKPV_K5km5, TextBoxKPV_K5TSV5, TextBoxKPV_K5TSV5edit)

        

    #     TextBoxKPV_K5TH1.Text = ""
    #     TextBoxKPV_K5TH2.Text = ""
    #     TextBoxKPV_K5TH3.Text = ""
    #     TextBoxKPV_K5TH4.Text = ""
    #     TextBoxKPV_K5TH5.Text = ""

    #     If TextBoxKPV_K5VHV1.Text <> "" And TextBoxKPV_K5TSV1edit.Text <> "" And TextBoxKPV_K5Cena1.Text <> "" Then
    #         If TextBoxKPV_K5VHMV1.Text <> "" And TextBoxKPV_K5TSMV1.Text <> "" Then
    #             TextBoxKPV_K5TH1.Text = FormatDoubleMoje(((CDblMoje(TextBoxKPV_K5VHV1.Text) * CDblMoje(TextBoxKPV_K5TSV1edit.Text)) / 100) + ((CDblMoje(TextBoxKPV_K5VHMV1.Text) * CDblMoje(TextBoxKPV_K5TSMV1.Text)) / 100), "# ##0.00")
    #         Else
    #             TextBoxKPV_K5TH1.Text = FormatDoubleMoje(((CDblMoje(TextBoxKPV_K5VHV1.Text) * CDblMoje(TextBoxKPV_K5TSV1edit.Text)) / 100), "# ##0.00")
    #         End If
    #     End If

    #     If TextBoxKPV_K5VHV2.Text <> "" And TextBoxKPV_K5TSV2edit.Text <> "" And TextBoxKPV_K5Cena2.Text <> "" Then
    #         If TextBoxKPV_K5VHMV2.Text <> "" And TextBoxKPV_K5TSMV2.Text <> "" Then
    #             TextBoxKPV_K5TH2.Text = FormatDoubleMoje(((CDblMoje(TextBoxKPV_K5VHV2.Text) * CDblMoje(TextBoxKPV_K5TSV2edit.Text)) / 100) + ((CDblMoje(TextBoxKPV_K5VHMV2.Text) * CDblMoje(TextBoxKPV_K5TSMV2.Text)) / 100), "# ##0.00")
    #         Else
    #             TextBoxKPV_K5TH2.Text = FormatDoubleMoje(((CDblMoje(TextBoxKPV_K5VHV2.Text) * CDblMoje(TextBoxKPV_K5TSV2edit.Text)) / 100), "# ##0.00")
    #         End If
    #     End If

    #     If TextBoxKPV_K5VHV3.Text <> "" And TextBoxKPV_K5TSV3edit.Text <> "" And TextBoxKPV_K5Cena3.Text <> "" Then
    #         If TextBoxKPV_K5VHMV3.Text <> "" And TextBoxKPV_K5TSMV3.Text <> "" Then
    #             TextBoxKPV_K5TH3.Text = FormatDoubleMoje(((CDblMoje(TextBoxKPV_K5VHV3.Text) * CDblMoje(TextBoxKPV_K5TSV3edit.Text)) / 100) + ((CDblMoje(TextBoxKPV_K5VHMV3.Text) * CDblMoje(TextBoxKPV_K5TSMV3.Text)) / 100), "# ##0.00")
    #         Else
    #             TextBoxKPV_K5TH3.Text = FormatDoubleMoje(((CDblMoje(TextBoxKPV_K5VHV3.Text) * CDblMoje(TextBoxKPV_K5TSV3edit.Text)) / 100), "# ##0.00")
    #         End If
    #     End If

    #     If TextBoxKPV_K5VHV4.Text <> "" And TextBoxKPV_K5TSV4edit.Text <> "" And TextBoxKPV_K5Cena4.Text <> "" Then
    #         If TextBoxKPV_K5VHMV4.Text <> "" And TextBoxKPV_K5TSMV4.Text <> "" Then
    #             TextBoxKPV_K5TH4.Text = FormatDoubleMoje(((CDblMoje(TextBoxKPV_K5VHV4.Text) * CDblMoje(TextBoxKPV_K5TSV4edit.Text)) / 100) + ((CDblMoje(TextBoxKPV_K5VHMV4.Text) * CDblMoje(TextBoxKPV_K5TSMV4.Text)) / 100), "# ##0.00")
    #         Else
    #             TextBoxKPV_K5TH4.Text = FormatDoubleMoje(((CDblMoje(TextBoxKPV_K5VHV4.Text) * CDblMoje(TextBoxKPV_K5TSV4edit.Text)) / 100), "# ##0.00")
    #         End If
    #     End If

    #     If TextBoxKPV_K5VHV5.Text <> "" And TextBoxKPV_K5TSV5edit.Text <> "" And TextBoxKPV_K5Cena5.Text <> "" Then
    #         If TextBoxKPV_K5VHMV5.Text <> "" And TextBoxKPV_K5TSMV5.Text <> "" Then
    #             TextBoxKPV_K5TH5.Text = FormatDoubleMoje(((CDblMoje(TextBoxKPV_K5VHV5.Text) * CDblMoje(TextBoxKPV_K5TSV5edit.Text)) / 100) + ((CDblMoje(TextBoxKPV_K5VHMV5.Text) * CDblMoje(TextBoxKPV_K5TSMV5.Text)) / 100), "# ##0.00")
    #         Else
    #             TextBoxKPV_K5TH5.Text = FormatDoubleMoje(((CDblMoje(TextBoxKPV_K5VHV5.Text) * CDblMoje(TextBoxKPV_K5TSV5edit.Text)) / 100), "# ##0.00")
    #         End If
    #     End If

    #     TextBoxKPVpriemPredajCena.Text = ""

    #     Dim tempCena As Double = 0
    #     Dim tempPocet As Double = 0

    #     If TextBoxKPV_K5Cena1.Text <> "" And TextBoxKPV_K5TH1.Text <> "" Then
    #         tempCena = tempCena + CDblMoje(TextBoxKPV_K5Cena1.Text)
    #         tempPocet = tempPocet + 1
    #     End If

    #     If TextBoxKPV_K5Cena2.Text <> "" And TextBoxKPV_K5TH2.Text <> "" Then
    #         tempCena = tempCena + CDblMoje(TextBoxKPV_K5Cena2.Text)
    #         tempPocet = tempPocet + 1
    #     End If

    #     If TextBoxKPV_K5Cena3.Text <> "" And TextBoxKPV_K5TH3.Text <> "" Then
    #         tempCena = tempCena + CDblMoje(TextBoxKPV_K5Cena3.Text)
    #         tempPocet = tempPocet + 1
    #     End If

    #     If TextBoxKPV_K5Cena4.Text <> "" And TextBoxKPV_K5TH4.Text <> "" Then
    #         tempCena = tempCena + CDblMoje(TextBoxKPV_K5Cena4.Text)
    #         tempPocet = tempPocet + 1
    #     End If

    #     If TextBoxKPV_K5Cena5.Text <> "" And TextBoxKPV_K5TH5.Text <> "" Then
    #         tempCena = tempCena + CDblMoje(TextBoxKPV_K5Cena5.Text)
    #         tempPocet = tempPocet + 1
    #     End If

    #     If tempPocet > 0 Then TextBoxKPVpriemPredajCena.Text = FormatDoubleMoje(tempCena / tempPocet, "# ##0.00")

    #     tempCena = 0
    #     tempPocet = 0
    #     TextBoxKPVpriemTechHodnVozidla.Text = ""

    #     If TextBoxKPV_K5TH1.Text <> "" Then
    #         tempCena = tempCena + CDblMoje(TextBoxKPV_K5TH1.Text)
    #         tempPocet = tempPocet + 1
    #     End If

    #     If TextBoxKPV_K5TH2.Text <> "" Then
    #         tempCena = tempCena + CDblMoje(TextBoxKPV_K5TH2.Text)
    #         tempPocet = tempPocet + 1
    #     End If

    #     If TextBoxKPV_K5TH3.Text <> "" Then
    #         tempCena = tempCena + CDblMoje(TextBoxKPV_K5TH3.Text)
    #         tempPocet = tempPocet + 1
    #     End If

    #     If TextBoxKPV_K5TH4.Text <> "" Then
    #         tempCena = tempCena + CDblMoje(TextBoxKPV_K5TH4.Text)
    #         tempPocet = tempPocet + 1
    #     End If

    #     If TextBoxKPV_K5TH5.Text <> "" Then
    #         tempCena = tempCena + CDblMoje(TextBoxKPV_K5TH5.Text)
    #         tempPocet = tempPocet + 1
    #     End If

    #     If tempPocet > 0 Then TextBoxKPVpriemTechHodnVozidla.Text = FormatDoubleMoje(tempCena / tempPocet, "# ##0.00")

    #     If (TextBoxKPVpriemPredajCena.Text = "" Or TextBoxKPVpriemTechHodnVozidla.Text = "") And TextBoxKPV_K5.Text = "" Then TextBoxKPV_K5.Text = "1,0000"
    #     If TextBoxKPVpriemTechHodnVozidla.Text <> "" And TextBoxKPVpriemPredajCena.Text <> "" Then TextBoxKPV_K5.Text = FormatDoubleMoje(CDblMoje(TextBoxKPVpriemPredajCena.Text) / CDblMoje(TextBoxKPVpriemTechHodnVozidla.Text), "0.0000")
    #     If TextBoxKPV_K5.Text = "" Then TextBoxKPV_K5.Text = "1,0000"

    #     Dim tempKP As Double = 1
    #     TextBoxKPV_Kp.Text = ""
    #     If TextBoxKPV_K1.Text <> "" Then tempKP = tempKP * CDblMoje(TextBoxKPV_K1.Text)
    #     If TextBoxKPV_K2.Text <> "" Then tempKP = tempKP * CDblMoje(TextBoxKPV_K2.Text)
    #     If TextBoxKPV_K3.Text <> "" Then tempKP = tempKP * CDblMoje(TextBoxKPV_K3.Text)
    #     If TextBoxKPV_K4.Text <> "" Then tempKP = tempKP * CDblMoje(TextBoxKPV_K4.Text)
    #     If TextBoxKPV_K5.Text <> "" Then tempKP = tempKP * CDblMoje(TextBoxKPV_K5.Text)
    #     TextBoxKPV_Kp.Text = FormatDoubleMoje(tempKP, "0.0000")

    #     TextBoxHV_VSH.Text = ""
    #     If TextBoxHV_TH.Text <> "" And TextBoxKPV_Kp.Text <> "" Then
    #         TextBoxHV_VSH.Text = FormatDoubleMoje(CDblMoje(TextBoxHV_TH.Text) * CDblMoje(TextBoxKPV_Kp.Text), "# ##0.00")
    #         TextBoxNNO_VSH.Text = TextBoxHV_VSH.Text
    #     End If