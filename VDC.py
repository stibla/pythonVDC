# importing wx files
import json
import wx

# import the newly created GUI file
import formVDCmain
import constantVDC
import functionVDC

import os

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
		self.TextBoxKPV_K5Cena1.SetValue("1 000")
		# test data end

		functionVDC.VypocitajDobuPrevadzky(self)

	def NovyVypocet(self, event):
		for item in vars(self).items():
			if(item[0][0:7] == "TextBox"):
				item[1].SetValue("")
			if(item[0][0:8] == "ComboBox"):
				item[1].SetStringSelection("")
			if(item[0][0:8] == "CheckBox"):
				item[1].SetValue(False)
		
		self.ComboBoxKategoriaMV.SetSelection(2)		
		self.ComboBoxKPV_poskodenie.SetSelection(0)
		functionVDC.VypocitajDobuPrevadzky(self)

	def OtvorZoSuboru(self, event):
		with wx.FileDialog(self, "VDC JSON fil", wildcard="VDC JSON files (*.vdcJSON)|*.vdcJson",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return    

			pathname = fileDialog.GetPath()
			try:
				with open(pathname, 'r') as json_file:
					dictData = json.load(json_file)
					self.NovyVypocet(None)
					for item in vars(self).items():
						if item[0] in dictData:
							if(item[0][0:7] == "TextBox"):
								item[1].SetValue(dictData[item[0]])
							if(item[0][0:8] == "ComboBox"):
								item[1].SetStringSelection(dictData[item[0]])
							if(item[0][0:8] == "CheckBox"):
								item[1].SetValue(dictData[item[0]])
				functionVDC.VypocitajDobuPrevadzky(self)
			except IOError:
				wx.LogError("Cannot open file '%s'." % pathname)
			except Exception as err:
				wx.MessageBox("Error: " + err.__str__(), "Attention",
                         wx.ICON_ERROR | wx.OK, self)	
	
	def ButtonUlozitToFileOnButtonClick(self, event):
		dictData = {}
		for item in vars(self).items():
			if(item[0][0:7] == "TextBox"):
				if(item[1].GetValue() != ""):
					dictData[item[0]] = item[1].GetValue()
			if(item[0][0:8] == "ComboBox"):			
				if(item[1].GetStringSelection() != ""):
					dictData[item[0]] = item[1].GetStringSelection()
			if(item[0][0:8] == "CheckBox"):
				dictData[item[0]] = item[1].IsChecked()
		
		with wx.FileDialog(self, "Save VDC JSON file", wildcard="VDC JSON files (*.vdcJSON)|*.vdcJson",
                       style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return     
			pathname = fileDialog.GetPath()
			try:
				with open(pathname, 'w') as file:
					json.dump(dictData, file, ensure_ascii=False)
			except IOError:
				wx.LogError("Cannot save current data in file '%s'." % pathname)

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
				if(x[i] != ""):
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
		if(event.GetEventObject().GetValue() == ""):
			exec("self.TextBoxTHVTSS" +
				 event.GetEventObject().GetName() + ".SetValue('')")
			exec("self.TextBoxTHPDS" +
				 event.GetEventObject().GetName() + ".SetValue('')")
			exec("self.TextBoxTHZAV" +
				 event.GetEventObject().GetName() + ".SetValue('')")
			exec("self.TextBoxTHZA" +
				 event.GetEventObject().GetName() + ".SetValue('')")
			exec("self.TextBoxTHZP" +
				 event.GetEventObject().GetName() + ".SetValue('')")
			exec("self.TextBoxTHTSS" +
				 event.GetEventObject().GetName() + ".SetValue('')")
			exec("self.TextBoxTHTSS" +
				 event.GetEventObject().GetName() + "edit.SetValue('')")

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
		if(event.GetEventObject().GetValue() == ""):
			exec("event.GetEventObject().SetValue(self.TextBoxTHTSS" +
				 event.GetEventObject().GetName() + ".GetValue())")
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
		functionVDC.PocitajVSH(self, "DatePickerTextBoxKPV_koniecTKOnDateChanged")

	def TextBoxKPV_koniecTKOnKillFocus(self, event):
		if (functionVDC.KontrolujDatum(event.GetEventObject())):
			functionVDC.PocitajVSH(self, "TextBoxKPV_koniecTKOnKillFocus")
			event.Skip()

	def ComboBoxKPV_poskodenieOnChoice(self, event):
		functionVDC.PocitajVSH(self, "ComboBoxKPV_poskodenieOnChoice")

 
	def TextBoxKPVPocetDrzitelovOnSpinCtrl(self, event):
		functionVDC.PocitajVSH(self, "TextBoxKPVPocetDrzitelovOnSpinCtrl")
	
	def CheckBoxKPVk3NezisteneOnCheckBox(self, event):
		if(self.CheckBoxKPVk3Nezistene.IsChecked()):
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
		if(constantVDC.pouzitiek4[i][16] != ""):
			self.LabelKPV_k1lehotaTKsuStazPodm.SetLabel(constantVDC.pouzitiek4[i][16])

		if(constantVDC.pouzitiek4[i][14] != "" and constantVDC.pouzitiek4[i][15] != "" ):
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
	
	def TextBoxKPV_K5VHVOnKillFocus( self, event ):
		if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 2)):
			exec('''if (self.TextBoxKPV_K5VHV''' + event.GetEventObject().GetName() + '''.GetValue() == '' and self.TextBoxKPV_K5Zdroj''' + event.GetEventObject().GetName() + '''.GetValue() != ''):
	self.TextBoxKPV_K5VHV''' + event.GetEventObject().GetName() + '''.SetValue(self.TextBoxHV_VHV.GetValue())''')
			functionVDC.PocitajVSH(self, "TextBoxKPV_K5VHVOnKillFocus")
			event.Skip()

	def TextBoxKPV_K5vPrevadzkeOnKillFocus(self, event):
		if (functionVDC.KontrolujDatum(event.GetEventObject())):
			functionVDC.PocitajVSH(self, "TextBoxKPV_K5vPrevadzkeOnKillFocus")
			event.Skip()     

	def TextBoxKPV_K5kmOnKillFocus( self, event ):
		if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 0)):
			functionVDC.PocitajVSH(self, "TextBoxKPV_K5kmOnKillFocus")
			event.Skip()

	def TextBoxKPV_K5CenaOnKillFocus( self, event ):
		if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 2)):
			functionVDC.PocitajVSH(self, "TextBoxKPV_K5CenaOnKillFocus")
			event.Skip()

	def TextBoxKPV_K5TSVeditOnKillFocus( self, event ):
		if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 4)):
			functionVDC.PocitajVSH(self, "TextBoxKPV_K5TSVeditOnKillFocus")
			event.Skip()

	def TextBoxKPV_K5VHMVOnKillFocus( self, event ):
		if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 2)):
			functionVDC.PocitajVSH(self, "TextBoxKPV_K5VHMVOnKillFocus")
			event.Skip()

	def TextBoxKPV_K5TSMVOnKillFocus( self, event ):
		if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 4)):
			functionVDC.PocitajVSH(self, "TextBoxKPV_K5TSMVOnKillFocus")
			event.Skip()

	def TextBoxKPV_K5OnKillFocus( self, event ):
		if (functionVDC.KontrolujFloatCislo(event.GetEventObject(), 4)):
			functionVDC.PocitajVSH(self, "TextBoxKPV_K5TSMVOnKillFocus")
			event.Skip()


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