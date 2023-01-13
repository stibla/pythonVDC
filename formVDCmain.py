# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.grid

###########################################################################
## Class VDCmain
###########################################################################

class VDCmain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"VDC - Vehicle Damage Calculation", pos = wx.DefaultPosition, size = wx.Size( 981,755 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.Size( -1,-1 ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		mainGbSizer = wx.GridBagSizer( 0, 0 )
		mainGbSizer.SetFlexibleDirection( wx.BOTH )
		mainGbSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.ButtonNovyVypocet = wx.Button( self, wx.ID_ANY, u"Nový výpočet", wx.DefaultPosition, wx.Size( -1,-1 ), 0, wx.DefaultValidator, u"ButtonNovyVypocet" )
		mainGbSizer.Add( self.ButtonNovyVypocet, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.ButtonOtvoritFromFile = wx.Button( self, wx.ID_ANY, u"Otvor zo súboru", wx.DefaultPosition, wx.Size( -1,-1 ), 0, wx.DefaultValidator, u"ButtonOtvoritFromFile" )
		mainGbSizer.Add( self.ButtonOtvoritFromFile, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.ButtonUlozitToFile = wx.Button( self, wx.ID_ANY, u"Ulož do súboru", wx.DefaultPosition, wx.Size( -1,-1 ), 0, wx.DefaultValidator, u"ButtonUlozitToFile" )
		mainGbSizer.Add( self.ButtonUlozitToFile, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.ButtonOtvoritZdb = wx.Button( self, wx.ID_ANY, u"Otvor z databázy", wx.DefaultPosition, wx.Size( -1,-1 ), 0, wx.DefaultValidator, u"ButtonOtvoritZdb" )
		mainGbSizer.Add( self.ButtonOtvoritZdb, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.ButtonUlozitDOdb = wx.Button( self, wx.ID_ANY, u"Ulož do databázy", wx.DefaultPosition, wx.Size( -1,-1 ), 0, wx.DefaultValidator, u"ButtonUlozitDOdb" )
		mainGbSizer.Add( self.ButtonUlozitDOdb, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.ButtonNNO_Tlac = wx.Button( self, wx.ID_ANY, u"Tlač", wx.DefaultPosition, wx.Size( -1,-1 ), 0, wx.DefaultValidator, u"ButtonNNO_Tlac" )
		mainGbSizer.Add( self.ButtonNNO_Tlac, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.ButtonTest = wx.Button( self, wx.ID_ANY, u"Test", wx.DefaultPosition, wx.DefaultSize, 0 )
		mainGbSizer.Add( self.ButtonTest, wx.GBPosition( 0, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.MultiPageVDC = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.MultiPageVDC.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		self.PageZakladneUdaje = wx.Panel( self.MultiPageVDC, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		GbSizerPageZakladneUdaje = wx.GridBagSizer( 0, 0 )
		GbSizerPageZakladneUdaje.SetFlexibleDirection( wx.BOTH )
		GbSizerPageZakladneUdaje.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.LabelCisloPripadu = wx.StaticText( self.PageZakladneUdaje, wx.ID_ANY, u"Číslo prípadu:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelCisloPripadu.Wrap( -1 )

		GbSizerPageZakladneUdaje.Add( self.LabelCisloPripadu, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 3 )

		self.TextBoxCisloPripadu = wx.TextCtrl( self.PageZakladneUdaje, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY, wx.DefaultValidator, u"TextBoxCisloPripadu" )
		GbSizerPageZakladneUdaje.Add( self.TextBoxCisloPripadu, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.LabelCPU = wx.StaticText( self.PageZakladneUdaje, wx.ID_ANY, u"Číslo PU:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelCPU.Wrap( -1 )

		GbSizerPageZakladneUdaje.Add( self.LabelCPU, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 3 )

		self.TextBoxCPU = wx.TextCtrl( self.PageZakladneUdaje, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0, wx.DefaultValidator, u"TextBoxCPU" )
		GbSizerPageZakladneUdaje.Add( self.TextBoxCPU, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.LabelDatumPU = wx.StaticText( self.PageZakladneUdaje, wx.ID_ANY, u"Dátum PU:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelDatumPU.Wrap( -1 )

		GbSizerPageZakladneUdaje.Add( self.LabelDatumPU, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 3 )

		GbSizerTextBoxDatumPU = wx.GridBagSizer( 0, 0 )
		GbSizerTextBoxDatumPU.SetFlexibleDirection( wx.BOTH )
		GbSizerTextBoxDatumPU.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.DateTimePickerDatumPU = wx.adv.DatePickerCtrl( self.PageZakladneUdaje, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 20,-1 ), wx.adv.DP_DROPDOWN )
		GbSizerTextBoxDatumPU.Add( self.DateTimePickerDatumPU, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM|wx.RIGHT, 3 )

		self.TextBoxDatumPU = wx.TextCtrl( self.PageZakladneUdaje, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxDatumPU" )
		self.TextBoxDatumPU.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.TextBoxDatumPU.SetMaxSize( wx.Size( 110,-1 ) )

		GbSizerTextBoxDatumPU.Add( self.TextBoxDatumPU, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.LEFT, 3 )


		GbSizerPageZakladneUdaje.Add( GbSizerTextBoxDatumPU, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.LabelPoskodeny = wx.StaticText( self.PageZakladneUdaje, wx.ID_ANY, u"Poškodený:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelPoskodeny.Wrap( -1 )

		GbSizerPageZakladneUdaje.Add( self.LabelPoskodeny, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 3 )

		self.TextBoxPoskodeny = wx.TextCtrl( self.PageZakladneUdaje, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0, wx.DefaultValidator, u"TextBoxPoskodeny" )
		GbSizerPageZakladneUdaje.Add( self.TextBoxPoskodeny, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 2 ), wx.ALL, 3 )

		self.CheckBoxPlatcaDPH = wx.CheckBox( self.PageZakladneUdaje, wx.ID_ANY, u"Platca DPH:", wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"CheckBoxPlatcaDPH" )
		GbSizerPageZakladneUdaje.Add( self.CheckBoxPlatcaDPH, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )

		self.LabelPoskodenyAdresa = wx.StaticText( self.PageZakladneUdaje, wx.ID_ANY, u"Adresa:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelPoskodenyAdresa.Wrap( -1 )

		GbSizerPageZakladneUdaje.Add( self.LabelPoskodenyAdresa, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 3 )

		self.TextBoxPoskodenyAdresa = wx.TextCtrl( self.PageZakladneUdaje, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 540,-1 ), 0, wx.DefaultValidator, u"TextBoxPoskodenyAdresa" )
		GbSizerPageZakladneUdaje.Add( self.TextBoxPoskodenyAdresa, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 4 ), wx.ALL, 3 )

		self.LabelUzivatelVytvoril = wx.StaticText( self.PageZakladneUdaje, wx.ID_ANY, u"Užívateľ vytvoril:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelUzivatelVytvoril.Wrap( -1 )

		GbSizerPageZakladneUdaje.Add( self.LabelUzivatelVytvoril, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 3 )

		self.TextBoxUzivatelVytvoril = wx.TextCtrl( self.PageZakladneUdaje, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY, wx.DefaultValidator, u"TextBoxUzivatelVytvoril" )
		GbSizerPageZakladneUdaje.Add( self.TextBoxUzivatelVytvoril, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 3 )

		self.LabelDatumVytvorenia = wx.StaticText( self.PageZakladneUdaje, wx.ID_ANY, u"Dátum:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelDatumVytvorenia.Wrap( -1 )

		GbSizerPageZakladneUdaje.Add( self.LabelDatumVytvorenia, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 3 )

		self.TextBoxDatumVytvorenia = wx.TextCtrl( self.PageZakladneUdaje, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY, wx.DefaultValidator, u"TextBoxDatumVytvorenia" )
		GbSizerPageZakladneUdaje.Add( self.TextBoxDatumVytvorenia, wx.GBPosition( 5, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 3 )

		self.LabelUzivatelZmenil = wx.StaticText( self.PageZakladneUdaje, wx.ID_ANY, u"Užívateľ zmenil:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelUzivatelZmenil.Wrap( -1 )

		GbSizerPageZakladneUdaje.Add( self.LabelUzivatelZmenil, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 3 )

		self.TextBoxUzivatelZmenil = wx.TextCtrl( self.PageZakladneUdaje, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY, wx.DefaultValidator, u"TextBoxUzivatelZmenil" )
		GbSizerPageZakladneUdaje.Add( self.TextBoxUzivatelZmenil, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 3 )

		self.LabelDatumZmeny = wx.StaticText( self.PageZakladneUdaje, wx.ID_ANY, u"Dátum:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelDatumZmeny.Wrap( -1 )

		GbSizerPageZakladneUdaje.Add( self.LabelDatumZmeny, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 3 )

		self.TextBoxDatumZmeny = wx.TextCtrl( self.PageZakladneUdaje, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY, wx.DefaultValidator, u"TextBoxDatumZmeny" )
		GbSizerPageZakladneUdaje.Add( self.TextBoxDatumZmeny, wx.GBPosition( 6, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 3 )

		self.LabelPoznamka = wx.StaticText( self.PageZakladneUdaje, wx.ID_ANY, u"Vyjadrenia/poznámka:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelPoznamka.Wrap( -1 )

		GbSizerPageZakladneUdaje.Add( self.LabelPoznamka, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_LEFT|wx.ALL, 3 )

		self.TextBoxPoznamka = wx.TextCtrl( self.PageZakladneUdaje, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_MULTILINE, wx.DefaultValidator, u"TextBoxPoznamka" )
		GbSizerPageZakladneUdaje.Add( self.TextBoxPoznamka, wx.GBPosition( 9, 0 ), wx.GBSpan( 15, 27 ), wx.ALL|wx.EXPAND, 3 )


		self.PageZakladneUdaje.SetSizer( GbSizerPageZakladneUdaje )
		self.PageZakladneUdaje.Layout()
		GbSizerPageZakladneUdaje.Fit( self.PageZakladneUdaje )
		self.MultiPageVDC.AddPage( self.PageZakladneUdaje, u"Základné údaje", True )
		self.PageVozidlo = wx.Panel( self.MultiPageVDC, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		GbSizerPageVozidlo = wx.GridBagSizer( 0, 0 )
		GbSizerPageVozidlo.SetFlexibleDirection( wx.BOTH )
		GbSizerPageVozidlo.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.LabelECV = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"Evidenčné číslo:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelECV.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelECV, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 3 )

		self.TextBoxECV = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxECV" )
		GbSizerPageVozidlo.Add( self.TextBoxECV, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 3 )

		self.LabelPridelenieECV = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"prvý krát pridelené:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelPridelenieECV.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelPridelenieECV, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 3 )

		GbSizerTextBoxPrideleneECV = wx.GridBagSizer( 0, 0 )
		GbSizerTextBoxPrideleneECV.SetFlexibleDirection( wx.BOTH )
		GbSizerTextBoxPrideleneECV.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.TextBoxPrideleneECV = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0, wx.DefaultValidator, u"TextBoxPrideleneECV" )
		self.TextBoxPrideleneECV.SetMaxSize( wx.Size( 110,-1 ) )

		GbSizerTextBoxPrideleneECV.Add( self.TextBoxPrideleneECV, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.DateTimePickerPrideleneECV = wx.adv.DatePickerCtrl( self.PageVozidlo, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 20,-1 ), wx.adv.DP_DROPDOWN )
		GbSizerTextBoxPrideleneECV.Add( self.DateTimePickerPrideleneECV, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )


		GbSizerPageVozidlo.Add( GbSizerTextBoxPrideleneECV, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.LabelKategoriaMV = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"Názov kategórie:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKategoriaMV.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelKategoriaMV, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 3 )

		ComboBoxKategoriaMVChoices = []
		self.ComboBoxKategoriaMV = wx.Choice( self.PageVozidlo, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ComboBoxKategoriaMVChoices, 0, wx.DefaultValidator, u"ComboBoxKategoriaMV" )
		self.ComboBoxKategoriaMV.SetSelection( 0 )
		self.ComboBoxKategoriaMV.SetMaxSize( wx.Size( 0,-1 ) )

		GbSizerPageVozidlo.Add( self.ComboBoxKategoriaMV, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 5 ), wx.ALL|wx.EXPAND, 3 )

		self.LabelPodkategoriaMV = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"podkategórie:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelPodkategoriaMV.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelPodkategoriaMV, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 3 )

		ComboBoxPodkategoriaMVChoices = []
		self.ComboBoxPodkategoriaMV = wx.Choice( self.PageVozidlo, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ComboBoxPodkategoriaMVChoices, 0, wx.DefaultValidator, u"ComboBoxPodkategoriaMV" )
		self.ComboBoxPodkategoriaMV.SetSelection( 0 )
		GbSizerPageVozidlo.Add( self.ComboBoxPodkategoriaMV, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 5 ), wx.ALL|wx.EXPAND, 3 )

		self.LabelZnackaMV = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"Značka, model, typ:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelZnackaMV.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelZnackaMV, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 3 )

		self.TextBoxZnackaMV = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxZnackaMV" )
		GbSizerPageVozidlo.Add( self.TextBoxZnackaMV, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.EXPAND, 3 )

		self.LabelVIN = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"VIN:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelVIN.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelVIN, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 3 )

		self.TextBoxVIN = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxVIN" )
		GbSizerPageVozidlo.Add( self.TextBoxVIN, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 3 )

		self.LabelCisloTP = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"Séria a číslo TP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelCisloTP.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelCisloTP, wx.GBPosition( 4, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 3 )

		self.TextBoxCisloTP = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxCisloTP" )
		GbSizerPageVozidlo.Add( self.TextBoxCisloTP, wx.GBPosition( 4, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 3 )

		self.LabelObjemMotora = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"Objem motora (ccm):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelObjemMotora.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelObjemMotora, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 3 )

		self.TextBoxObjemMotora = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxObjemMotora" )
		GbSizerPageVozidlo.Add( self.TextBoxObjemMotora, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 3 )

		self.LabelVykon = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"Výkon (kW):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelVykon.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelVykon, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 3 )

		self.TextBoxVykon = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxVykon" )
		GbSizerPageVozidlo.Add( self.TextBoxVykon, wx.GBPosition( 5, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 3 )

		self.LabelOtacky = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"pri otáčkach:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelOtacky.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelOtacky, wx.GBPosition( 5, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 3 )

		self.TextBoxOtacky = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxOtacky" )
		GbSizerPageVozidlo.Add( self.TextBoxOtacky, wx.GBPosition( 5, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 3 )

		self.LabelCisloMotora = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"Číslo motora:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelCisloMotora.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelCisloMotora, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 3 )

		self.TextBoxCisloMotora = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxCisloMotora" )
		GbSizerPageVozidlo.Add( self.TextBoxCisloMotora, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 3 )

		self.LabelCisloRamu = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"číslo rámu:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelCisloRamu.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelCisloRamu, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 3 )

		self.TextBoxCisloRamu = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxCisloRamu" )
		GbSizerPageVozidlo.Add( self.TextBoxCisloRamu, wx.GBPosition( 6, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 3 )

		self.LabelPalivo = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"Palivo:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelPalivo.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelPalivo, wx.GBPosition( 6, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 3 )

		ComboBoxPalivoChoices = []
		self.ComboBoxPalivo = wx.Choice( self.PageVozidlo, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ComboBoxPalivoChoices, 0, wx.DefaultValidator, u"ComboBoxPalivo" )
		self.ComboBoxPalivo.SetSelection( 0 )
		self.ComboBoxPalivo.SetMaxSize( wx.Size( 0,-1 ) )

		GbSizerPageVozidlo.Add( self.ComboBoxPalivo, wx.GBPosition( 6, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.LabelHmotnostCelkova = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"Hmotnosť celková (kg):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelHmotnostCelkova.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelHmotnostCelkova, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 3 )

		self.TextBoxHmotnostCelkova = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxHmotnostCelkova" )
		GbSizerPageVozidlo.Add( self.TextBoxHmotnostCelkova, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 3 )

		self.LabelPohotovostnaHmotnost = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"pohotovostná (kg):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelPohotovostnaHmotnost.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelPohotovostnaHmotnost, wx.GBPosition( 7, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 3 )

		self.TextBoxPohotovostnaHmotnost = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxPohotovostnaHmotnost" )
		GbSizerPageVozidlo.Add( self.TextBoxPohotovostnaHmotnost, wx.GBPosition( 7, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 3 )

		self.LabelPocetNaprav = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"Počet náprav/kolies:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelPocetNaprav.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelPocetNaprav, wx.GBPosition( 7, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 3 )

		self.TextBoxPocetNaprav = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxPocetNaprav" )
		GbSizerPageVozidlo.Add( self.TextBoxPocetNaprav, wx.GBPosition( 7, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 3 )

		self.LabelCelkovaDlzka = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"Celková dĺžka (mm):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelCelkovaDlzka.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelCelkovaDlzka, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 3 )

		self.TextBoxCelkovaDlzka = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxCelkovaDlzka" )
		GbSizerPageVozidlo.Add( self.TextBoxCelkovaDlzka, wx.GBPosition( 8, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 3 )

		self.LabelRazvor = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"Rázvor (mm):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelRazvor.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelRazvor, wx.GBPosition( 8, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 3 )

		self.TextBoxRazvor = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxRazvor" )
		GbSizerPageVozidlo.Add( self.TextBoxRazvor, wx.GBPosition( 8, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 3 )

		self.LabelPocetDveri = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"Počet dverí/miest:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelPocetDveri.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelPocetDveri, wx.GBPosition( 8, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 3 )

		self.TextBoxPocetDveri = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxPocetDveri" )
		GbSizerPageVozidlo.Add( self.TextBoxPocetDveri, wx.GBPosition( 8, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 3 )

		self.LabelOdjazdene = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"Odjazdené km/motohod:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelOdjazdene.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelOdjazdene, wx.GBPosition( 9, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 3 )

		self.TextBoxOdjazdene = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxOdjazdene" )
		GbSizerPageVozidlo.Add( self.TextBoxOdjazdene, wx.GBPosition( 9, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 3 )

		self.LabelFarba = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"Farba/druh laku:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelFarba.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelFarba, wx.GBPosition( 9, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 3 )

		self.TextBoxFarba = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxFarba" )
		GbSizerPageVozidlo.Add( self.TextBoxFarba, wx.GBPosition( 9, 3 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 3 )

		self.LabelRokVyrobyMV = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"Rok výroby:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelRokVyrobyMV.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelRokVyrobyMV, wx.GBPosition( 10, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 3 )

		self.TextBoxRokVyrobyMV = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxRokVyrobyMV" )
		GbSizerPageVozidlo.Add( self.TextBoxRokVyrobyMV, wx.GBPosition( 10, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 3 )

		self.LabelVprevadzkeOd = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"v prevadzke od:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelVprevadzkeOd.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelVprevadzkeOd, wx.GBPosition( 10, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 3 )

		GbSizerTextBoxVprevadzkeOd = wx.GridBagSizer( 0, 0 )
		GbSizerTextBoxVprevadzkeOd.SetFlexibleDirection( wx.BOTH )
		GbSizerTextBoxVprevadzkeOd.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.TextBoxVprevadzkeOd = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxVprevadzkeOd" )
		self.TextBoxVprevadzkeOd.SetMaxSize( wx.Size( 110,-1 ) )

		GbSizerTextBoxVprevadzkeOd.Add( self.TextBoxVprevadzkeOd, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.LEFT, 3 )

		self.DateTimePickerVprevadzkeOd = wx.adv.DatePickerCtrl( self.PageVozidlo, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 20,-1 ), wx.adv.DP_DROPDOWN )
		GbSizerTextBoxVprevadzkeOd.Add( self.DateTimePickerVprevadzkeOd, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT, 3 )


		GbSizerPageVozidlo.Add( GbSizerTextBoxVprevadzkeOd, wx.GBPosition( 10, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.LabelTobaPrevadzkyT = wx.StaticText( self.PageVozidlo, wx.ID_ANY, u"doba prevádzky mesiace (T):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTobaPrevadzkyT.Wrap( -1 )

		GbSizerPageVozidlo.Add( self.LabelTobaPrevadzkyT, wx.GBPosition( 10, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 3 )

		self.TextBoxDobaPrevadzkyMesiac = wx.TextCtrl( self.PageVozidlo, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxDobaPrevadzkyMesiac" )
		GbSizerPageVozidlo.Add( self.TextBoxDobaPrevadzkyMesiac, wx.GBPosition( 10, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 3 )

		FramePneumatiky = wx.StaticBoxSizer( wx.StaticBox( self.PageVozidlo, wx.ID_ANY, u"Pneumatiky" ), wx.VERTICAL )

		FramePneumatikyGbSizer = wx.GridBagSizer( 0, 0 )
		FramePneumatikyGbSizer.SetFlexibleDirection( wx.BOTH )
		FramePneumatikyGbSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.LabelPneuPocet = wx.StaticText( FramePneumatiky.GetStaticBox(), wx.ID_ANY, u"Počet", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelPneuPocet.Wrap( -1 )

		FramePneumatikyGbSizer.Add( self.LabelPneuPocet, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.LabelPneuPopis = wx.StaticText( FramePneumatiky.GetStaticBox(), wx.ID_ANY, u"Popis", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelPneuPopis.Wrap( -1 )

		FramePneumatikyGbSizer.Add( self.LabelPneuPopis, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.LabelPneuPriamaTH = wx.StaticText( FramePneumatiky.GetStaticBox(), wx.ID_ANY, u"Priama TH %", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelPneuPriamaTH.Wrap( -1 )

		FramePneumatikyGbSizer.Add( self.LabelPneuPriamaTH, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.LabelPneuNamerane = wx.StaticText( FramePneumatiky.GetStaticBox(), wx.ID_ANY, u"Namerané mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelPneuNamerane.Wrap( -1 )

		FramePneumatikyGbSizer.Add( self.LabelPneuNamerane, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.LabelPneuNove = wx.StaticText( FramePneumatiky.GetStaticBox(), wx.ID_ANY, u"Nové mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelPneuNove.Wrap( -1 )

		FramePneumatikyGbSizer.Add( self.LabelPneuNove, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.LabelPneuTH = wx.StaticText( FramePneumatiky.GetStaticBox(), wx.ID_ANY, u"TH %", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelPneuTH.Wrap( -1 )

		FramePneumatikyGbSizer.Add( self.LabelPneuTH, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.TextBoxPneuPocet1 = wx.TextCtrl( FramePneumatiky.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxPneuPocet" )
		FramePneumatikyGbSizer.Add( self.TextBoxPneuPocet1, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.TextBoxPneuPopis1 = wx.TextCtrl( FramePneumatiky.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0, wx.DefaultValidator, u"TextBoxPneuPopis" )
		FramePneumatikyGbSizer.Add( self.TextBoxPneuPopis1, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.TextBoxPneuPriamaTH1 = wx.TextCtrl( FramePneumatiky.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxPneuPriamaTH" )
		FramePneumatikyGbSizer.Add( self.TextBoxPneuPriamaTH1, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.TextBoxPneuNamerane1 = wx.TextCtrl( FramePneumatiky.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxPneuNamerane" )
		FramePneumatikyGbSizer.Add( self.TextBoxPneuNamerane1, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.TextBoxPneuNove1 = wx.TextCtrl( FramePneumatiky.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxPneuNove" )
		FramePneumatikyGbSizer.Add( self.TextBoxPneuNove1, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.TextBoxPneuTH1 = wx.TextCtrl( FramePneumatiky.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxPneuTH" )
		FramePneumatikyGbSizer.Add( self.TextBoxPneuTH1, wx.GBPosition( 1, 5 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.TextBoxPneuPocet2 = wx.TextCtrl( FramePneumatiky.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxPneuPocet" )
		FramePneumatikyGbSizer.Add( self.TextBoxPneuPocet2, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.TextBoxPneuPopis2 = wx.TextCtrl( FramePneumatiky.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxPneuPopis" )
		FramePneumatikyGbSizer.Add( self.TextBoxPneuPopis2, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.TextBoxPneuPriamaTH2 = wx.TextCtrl( FramePneumatiky.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxPneuPriamaTH" )
		FramePneumatikyGbSizer.Add( self.TextBoxPneuPriamaTH2, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.TextBoxPneuNamerane2 = wx.TextCtrl( FramePneumatiky.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxPneuNamerane" )
		FramePneumatikyGbSizer.Add( self.TextBoxPneuNamerane2, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.TextBoxPneuNove2 = wx.TextCtrl( FramePneumatiky.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxPneuNove" )
		FramePneumatikyGbSizer.Add( self.TextBoxPneuNove2, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.TextBoxPneuTH2 = wx.TextCtrl( FramePneumatiky.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxPneuTH" )
		FramePneumatikyGbSizer.Add( self.TextBoxPneuTH2, wx.GBPosition( 2, 5 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.TextBoxPneuPocet3 = wx.TextCtrl( FramePneumatiky.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxPneuPocet" )
		FramePneumatikyGbSizer.Add( self.TextBoxPneuPocet3, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.TextBoxPneuPopis3 = wx.TextCtrl( FramePneumatiky.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxPneuPopis" )
		FramePneumatikyGbSizer.Add( self.TextBoxPneuPopis3, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.TextBoxPneuPriamaTH3 = wx.TextCtrl( FramePneumatiky.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxPneuPriamaTH" )
		FramePneumatikyGbSizer.Add( self.TextBoxPneuPriamaTH3, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.TextBoxPneuNamerane3 = wx.TextCtrl( FramePneumatiky.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxPneuNamerane" )
		FramePneumatikyGbSizer.Add( self.TextBoxPneuNamerane3, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.TextBoxPneuNove3 = wx.TextCtrl( FramePneumatiky.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxPneuNove" )
		FramePneumatikyGbSizer.Add( self.TextBoxPneuNove3, wx.GBPosition( 3, 4 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.TextBoxPneuTH3 = wx.TextCtrl( FramePneumatiky.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxPneuTH" )
		FramePneumatikyGbSizer.Add( self.TextBoxPneuTH3, wx.GBPosition( 3, 5 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.TextBoxPneuTH = wx.TextCtrl( FramePneumatiky.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxPneuTHcelk" )
		FramePneumatikyGbSizer.Add( self.TextBoxPneuTH, wx.GBPosition( 4, 5 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


		FramePneumatiky.Add( FramePneumatikyGbSizer, 1, wx.EXPAND, 5 )


		GbSizerPageVozidlo.Add( FramePneumatiky, wx.GBPosition( 11, 0 ), wx.GBSpan( 1, 6 ), wx.EXPAND, 5 )


		self.PageVozidlo.SetSizer( GbSizerPageVozidlo )
		self.PageVozidlo.Layout()
		GbSizerPageVozidlo.Fit( self.PageVozidlo )
		self.MultiPageVDC.AddPage( self.PageVozidlo, u"Vozidlo", False )
		self.PageTechnickaHodnota = wx.Panel( self.MultiPageVDC, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		GbSizerPageTechnickaHodnota = wx.GridBagSizer( 0, 0 )
		GbSizerPageTechnickaHodnota.SetFlexibleDirection( wx.BOTH )
		GbSizerPageTechnickaHodnota.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.LabelTHdobaPrevadzky = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"doba prevádzky mesiace (T):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHdobaPrevadzky.Wrap( -1 )

		GbSizerPageTechnickaHodnota.Add( self.LabelTHdobaPrevadzky, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )

		self.TextBoxTHdobaPrevadzky = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHdobaPrevadzky" )
		GbSizerPageTechnickaHodnota.Add( self.TextBoxTHdobaPrevadzky, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )

		self.LabelTHZAVa = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"LabelTHZAVa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHZAVa.Wrap( -1 )

		self.LabelTHZAVa.Hide()

		GbSizerPageTechnickaHodnota.Add( self.LabelTHZAVa, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.LabelTHPKV = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"Predpokladaný ročný jazdný výkon v km/rok (PKV):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHPKV.Wrap( -1 )

		GbSizerPageTechnickaHodnota.Add( self.LabelTHPKV, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )

		self.TextBoxTHPKV = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPKV" )
		GbSizerPageTechnickaHodnota.Add( self.TextBoxTHPKV, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 2 )

		self.LabelTHZAVb = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"LabelTHZAVb", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHZAVb.Wrap( -1 )

		self.LabelTHZAVb.Hide()

		GbSizerPageTechnickaHodnota.Add( self.LabelTHZAVb, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.LabelTHPZTS = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"Predpokladaný zostatkový technický stav v % (PZTS):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHPZTS.Wrap( -1 )

		GbSizerPageTechnickaHodnota.Add( self.LabelTHPZTS, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )

		self.TextBoxTHPZTS = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPZTS" )
		GbSizerPageTechnickaHodnota.Add( self.TextBoxTHPZTS, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 2 )

		self.LabelTHZAVc = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"LabelTHZAVc", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHZAVc.Wrap( -1 )

		self.LabelTHZAVc.Hide()

		GbSizerPageTechnickaHodnota.Add( self.LabelTHZAVc, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.LabelTHPEZ = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"Predpokladaná efektívna životnosť v rokoch (PEZ):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHPEZ.Wrap( -1 )

		GbSizerPageTechnickaHodnota.Add( self.LabelTHPEZ, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )

		self.TextBoxTHPEZ = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPEZ" )
		GbSizerPageTechnickaHodnota.Add( self.TextBoxTHPEZ, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 2 )

		self.LabelTHZAVd = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"LabelTHZAVd", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHZAVd.Wrap( -1 )

		self.LabelTHZAVd.Enable( False )

		GbSizerPageTechnickaHodnota.Add( self.LabelTHZAVd, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.LabelTHPRKM = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"Predpokladaný počet najazdených kilometrov (PRKM):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHPRKM.Wrap( -1 )

		GbSizerPageTechnickaHodnota.Add( self.LabelTHPRKM, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )

		self.TextBoxTHPRKM = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPRKM" )
		GbSizerPageTechnickaHodnota.Add( self.TextBoxTHPRKM, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 2 )

		self.LabelTHRKM = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"Rozdiel v počte najazdených kilometrov (RKM):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHRKM.Wrap( -1 )

		GbSizerPageTechnickaHodnota.Add( self.LabelTHRKM, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )

		self.TextBoxTHRKM = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHRKM" )
		GbSizerPageTechnickaHodnota.Add( self.TextBoxTHRKM, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 2 )

		self.LabelTHkKM = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"Koeficient najazdených kilometrov (kKM):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHkKM.Wrap( -1 )

		GbSizerPageTechnickaHodnota.Add( self.LabelTHkKM, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )

		self.TextBoxTHkKM = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHkKM" )
		GbSizerPageTechnickaHodnota.Add( self.TextBoxTHkKM, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 2 )

		self.LabelTHkAM = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"Koeficient amortizácie za skutočne najazdené kilometre (kAM):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHkAM.Wrap( -1 )

		GbSizerPageTechnickaHodnota.Add( self.LabelTHkAM, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )

		self.TextBoxTHkAM = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHkAM" )
		GbSizerPageTechnickaHodnota.Add( self.TextBoxTHkAM, wx.GBPosition( 7, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 2 )

		self.LabelTHRozdelitNaSkupiny = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"Rozdelit skupiny:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHRozdelitNaSkupiny.Wrap( -1 )

		GbSizerPageTechnickaHodnota.Add( self.LabelTHRozdelitNaSkupiny, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )

		ComboBoxTHRozdelitSkupinyChoices = []
		self.ComboBoxTHRozdelitSkupiny = wx.Choice( self.PageTechnickaHodnota, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ComboBoxTHRozdelitSkupinyChoices, 0, wx.DefaultValidator, u"ComboBoxTHRozdelitSkupiny" )
		self.ComboBoxTHRozdelitSkupiny.SetSelection( 0 )
		GbSizerPageTechnickaHodnota.Add( self.ComboBoxTHRozdelitSkupiny, wx.GBPosition( 8, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 2 )

		GbSizertechnickaHodnota = wx.GridBagSizer( 0, 0 )
		GbSizertechnickaHodnota.SetFlexibleDirection( wx.BOTH )
		GbSizertechnickaHodnota.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.LabelTHskupina = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"Skupina", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHskupina.Wrap( -1 )

		GbSizertechnickaHodnota.Add( self.LabelTHskupina, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 0 )

		self.LabelTHVTSS = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"VTSS %", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHVTSS.Wrap( -1 )

		GbSizertechnickaHodnota.Add( self.LabelTHVTSS, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		self.LabelTHZAV = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"ZAV %", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHZAV.Wrap( -1 )

		GbSizertechnickaHodnota.Add( self.LabelTHZAV, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		self.LabelTHZA = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"ZA %", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHZA.Wrap( -1 )

		GbSizertechnickaHodnota.Add( self.LabelTHZA, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		self.LabelTHZP = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"ZP %", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHZP.Wrap( -1 )

		GbSizertechnickaHodnota.Add( self.LabelTHZP, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		self.LabelTHTSS = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"TSS %", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHTSS.Wrap( -1 )

		GbSizertechnickaHodnota.Add( self.LabelTHTSS, wx.GBPosition( 0, 6 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		self.LabelTHPTSS = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"PTSS %", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHPTSS.Wrap( -1 )

		GbSizertechnickaHodnota.Add( self.LabelTHPTSS, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		self.LabelTHPDS = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"PDS %", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHPDS.Wrap( -1 )

		GbSizertechnickaHodnota.Add( self.LabelTHPDS, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		self.TextBoxTHSkupina1 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0, wx.DefaultValidator, u"TextBoxTHSkupina#1" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHSkupina1, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxTHVTSS1 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHVTSS#1" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHVTSS1, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHPDS1 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPDS#1" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHPDS1, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZAV1 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZAV#1" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZAV1, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZA1 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZA#1" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZA1, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZP1 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZP#1" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZP1, wx.GBPosition( 1, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHTSS1 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0, wx.DefaultValidator, u"1" )
		self.TextBoxTHTSS1.Hide()

		GbSizertechnickaHodnota.Add( self.TextBoxTHTSS1, wx.GBPosition( 1, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHTSS1edit = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHTSS#1" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHTSS1edit, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHPTSS1 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPTSS#1" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHPTSS1, wx.GBPosition( 1, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHSkupina2 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxTHSkupina#2" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHSkupina2, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxTHVTSS2 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHVTSS#2" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHVTSS2, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHPDS2 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPDS#2" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHPDS2, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZAV2 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZAV#2" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZAV2, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZA2 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZA#2" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZA2, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZP2 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZP#2" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZP2, wx.GBPosition( 2, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHTSS2 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0, wx.DefaultValidator, u"2" )
		self.TextBoxTHTSS2.Hide()

		GbSizertechnickaHodnota.Add( self.TextBoxTHTSS2, wx.GBPosition( 2, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHTSS2edit = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHTSS#2" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHTSS2edit, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHPTSS2 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPTSS#2" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHPTSS2, wx.GBPosition( 2, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHSkupina3 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxTHSkupina#3" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHSkupina3, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxTHVTSS3 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHVTSS#3" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHVTSS3, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHPDS3 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPDS#3" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHPDS3, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZAV3 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZAV#3" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZAV3, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZA3 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZA#3" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZA3, wx.GBPosition( 3, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZP3 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZP#3" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZP3, wx.GBPosition( 3, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHTSS3edit = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHTSS#3" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHTSS3edit, wx.GBPosition( 3, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHPTSS3 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPTSS#3" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHPTSS3, wx.GBPosition( 3, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHTSS3 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0, wx.DefaultValidator, u"3" )
		self.TextBoxTHTSS3.Hide()

		GbSizertechnickaHodnota.Add( self.TextBoxTHTSS3, wx.GBPosition( 3, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHSkupina4 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxTHSkupina#4" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHSkupina4, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxTHVTSS4 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHVTSS#4" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHVTSS4, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHPDS4 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPDS#4" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHPDS4, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZAV4 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZAV#4" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZAV4, wx.GBPosition( 4, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZA4 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZA#4" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZA4, wx.GBPosition( 4, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZP4 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZP#4" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZP4, wx.GBPosition( 4, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHTSS4edit = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHTSS#4" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHTSS4edit, wx.GBPosition( 4, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHPTSS4 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPTSS#4" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHPTSS4, wx.GBPosition( 4, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHTSS4 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0, wx.DefaultValidator, u"4" )
		self.TextBoxTHTSS4.Hide()

		GbSizertechnickaHodnota.Add( self.TextBoxTHTSS4, wx.GBPosition( 4, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHSkupina5 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxTHSkupina#5" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHSkupina5, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxTHVTSS5 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHVTSS#5" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHVTSS5, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHPDS5 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPDS#5" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHPDS5, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZAV5 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZAV#5" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZAV5, wx.GBPosition( 5, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZA5 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZA#5" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZA5, wx.GBPosition( 5, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZP5 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZP#5" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZP5, wx.GBPosition( 5, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHTSS5edit = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHTSS#5" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHTSS5edit, wx.GBPosition( 5, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHPTSS5 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPTSS#5" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHPTSS5, wx.GBPosition( 5, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHTSS5 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0, wx.DefaultValidator, u"5" )
		self.TextBoxTHTSS5.Hide()

		GbSizertechnickaHodnota.Add( self.TextBoxTHTSS5, wx.GBPosition( 5, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHSkupina6 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxTHSkupina#6" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHSkupina6, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxTHVTSS6 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHVTSS#6" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHVTSS6, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHPDS6 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPDS#6" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHPDS6, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZAV6 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZAV#6" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZAV6, wx.GBPosition( 6, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZA6 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZA#6" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZA6, wx.GBPosition( 6, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZP6 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZP#6" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZP6, wx.GBPosition( 6, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHTSS6edit = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHTSS#6" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHTSS6edit, wx.GBPosition( 6, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHPTSS6 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPTSS#6" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHPTSS6, wx.GBPosition( 6, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHTSS6 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0, wx.DefaultValidator, u"6" )
		self.TextBoxTHTSS6.Hide()

		GbSizertechnickaHodnota.Add( self.TextBoxTHTSS6, wx.GBPosition( 6, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHSkupina7 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxTHSkupina#7" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHSkupina7, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxTHVTSS7 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHVTSS#7" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHVTSS7, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHPDS7 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPDS#7" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHPDS7, wx.GBPosition( 7, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZAV7 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZAV#7" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZAV7, wx.GBPosition( 7, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZA7 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZA#7" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZA7, wx.GBPosition( 7, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZP7 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZP#7" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZP7, wx.GBPosition( 7, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHTSS7edit = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHTSS#7" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHTSS7edit, wx.GBPosition( 7, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHPTSS7 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPTSS#7" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHPTSS7, wx.GBPosition( 7, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHTSS7 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0, wx.DefaultValidator, u"7" )
		self.TextBoxTHTSS7.Hide()

		GbSizertechnickaHodnota.Add( self.TextBoxTHTSS7, wx.GBPosition( 7, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHSkupina8 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxTHSkupina#8" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHSkupina8, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxTHVTSS8 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHVTSS#8" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHVTSS8, wx.GBPosition( 8, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHPDS8 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPDS#8" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHPDS8, wx.GBPosition( 8, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZAV8 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZAV#8" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZAV8, wx.GBPosition( 8, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZA8 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZA#8" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZA8, wx.GBPosition( 8, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZP8 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZP#8" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZP8, wx.GBPosition( 8, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHTSS8edit = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHTSS#8" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHTSS8edit, wx.GBPosition( 8, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHPTSS8 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPTSS#8" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHPTSS8, wx.GBPosition( 8, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHTSS8 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0, wx.DefaultValidator, u"8" )
		self.TextBoxTHTSS8.Hide()

		GbSizertechnickaHodnota.Add( self.TextBoxTHTSS8, wx.GBPosition( 8, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHSkupina9 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxTHSkupina#9" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHSkupina9, wx.GBPosition( 9, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxTHVTSS9 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHVTSS#9" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHVTSS9, wx.GBPosition( 9, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHPDS9 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPDS#9" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHPDS9, wx.GBPosition( 9, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZAV9 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZAV#9" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZAV9, wx.GBPosition( 9, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZA9 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZA#9" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZA9, wx.GBPosition( 9, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHZP9 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHZP#9" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHZP9, wx.GBPosition( 9, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHTSS9edit = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHTSS#9" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHTSS9edit, wx.GBPosition( 9, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHPTSS9 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPTSS#9" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHPTSS9, wx.GBPosition( 9, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHTSS9 = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0, wx.DefaultValidator, u"9" )
		self.TextBoxTHTSS9.Hide()

		GbSizertechnickaHodnota.Add( self.TextBoxTHTSS9, wx.GBPosition( 9, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxTHPDSSpolu = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHPDSSpolu" )
		self.TextBoxTHPDSSpolu.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		GbSizertechnickaHodnota.Add( self.TextBoxTHPDSSpolu, wx.GBPosition( 10, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.LabelTHTSV = wx.StaticText( self.PageTechnickaHodnota, wx.ID_ANY, u"Technický stav vozidla (TSV):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelTHTSV.Wrap( -1 )

		GbSizertechnickaHodnota.Add( self.LabelTHTSV, wx.GBPosition( 10, 4 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0 )

		self.TextBoxTHTSV = wx.TextCtrl( self.PageTechnickaHodnota, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxTHTSV" )
		GbSizertechnickaHodnota.Add( self.TextBoxTHTSV, wx.GBPosition( 10, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )


		GbSizerPageTechnickaHodnota.Add( GbSizertechnickaHodnota, wx.GBPosition( 9, 0 ), wx.GBSpan( 1, 3 ), wx.EXPAND, 5 )


		self.PageTechnickaHodnota.SetSizer( GbSizerPageTechnickaHodnota )
		self.PageTechnickaHodnota.Layout()
		GbSizerPageTechnickaHodnota.Fit( self.PageTechnickaHodnota )
		self.MultiPageVDC.AddPage( self.PageTechnickaHodnota, u"Technická hodnota", False )
		self.PageHodnotaVozidla = wx.Panel( self.MultiPageVDC, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		GbSizerPageHodnotaVozidla = wx.GridBagSizer( 0, 0 )
		GbSizerPageHodnotaVozidla.SetFlexibleDirection( wx.BOTH )
		GbSizerPageHodnotaVozidla.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.LabelHV_VHV = wx.StaticText( self.PageHodnotaVozidla, wx.ID_ANY, u"Východisková hodnota vozidla (VHV):", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.LabelHV_VHV.Wrap( -1 )

		GbSizerPageHodnotaVozidla.Add( self.LabelHV_VHV, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 2 )

		self.TextBoxHV_VHV = wx.TextCtrl( self.PageHodnotaVozidla, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxHV_VHV" )
		GbSizerPageHodnotaVozidla.Add( self.TextBoxHV_VHV, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 2 )

		self.LabelKPV_k1a = wx.StaticText( self.PageHodnotaVozidla, wx.ID_ANY, u"LabelKPV_k1a", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPV_k1a.Wrap( -1 )

		self.LabelKPV_k1a.Hide()

		GbSizerPageHodnotaVozidla.Add( self.LabelKPV_k1a, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.LabelHV_TSV = wx.StaticText( self.PageHodnotaVozidla, wx.ID_ANY, u"Technický stav vozidla (TSV):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelHV_TSV.Wrap( -1 )

		GbSizerPageHodnotaVozidla.Add( self.LabelHV_TSV, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 2 )

		self.TextBoxHV_TSV = wx.TextCtrl( self.PageHodnotaVozidla, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxHV_TSV" )
		GbSizerPageHodnotaVozidla.Add( self.TextBoxHV_TSV, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 2 )

		self.LabelKPV_k1b = wx.StaticText( self.PageHodnotaVozidla, wx.ID_ANY, u"LabelKPV_k1b", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPV_k1b.Wrap( -1 )

		self.LabelKPV_k1b.Hide()

		GbSizerPageHodnotaVozidla.Add( self.LabelKPV_k1b, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.LabelHV_VHMV = wx.StaticText( self.PageHodnotaVozidla, wx.ID_ANY, u"Východisková  hodnota mimoriadnej výbavy (VHMV):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelHV_VHMV.Wrap( -1 )

		GbSizerPageHodnotaVozidla.Add( self.LabelHV_VHMV, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 2 )

		self.TextBoxHV_VHMV = wx.TextCtrl( self.PageHodnotaVozidla, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxHV_VHMV" )
		GbSizerPageHodnotaVozidla.Add( self.TextBoxHV_VHMV, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 2 )

		self.LabelKPV_k1lehotaTK = wx.StaticText( self.PageHodnotaVozidla, wx.ID_ANY, u"LabelKPV_k1lehotaTK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPV_k1lehotaTK.Wrap( -1 )

		self.LabelKPV_k1lehotaTK.Hide()

		GbSizerPageHodnotaVozidla.Add( self.LabelKPV_k1lehotaTK, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.LabelHV_TSMV = wx.StaticText( self.PageHodnotaVozidla, wx.ID_ANY, u"Technický stav mimoriadnej výbavy (TSMV):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelHV_TSMV.Wrap( -1 )

		GbSizerPageHodnotaVozidla.Add( self.LabelHV_TSMV, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 2 )

		self.TextBoxHV_TSMV = wx.TextCtrl( self.PageHodnotaVozidla, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxHV_TSMV" )
		GbSizerPageHodnotaVozidla.Add( self.TextBoxHV_TSMV, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 2 )

		self.LabelKPV_k1lehotaTKstazPodm = wx.StaticText( self.PageHodnotaVozidla, wx.ID_ANY, u"LabelKPV_k1lehotaTKstazPodm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPV_k1lehotaTKstazPodm.Wrap( -1 )

		self.LabelKPV_k1lehotaTKstazPodm.Hide()

		GbSizerPageHodnotaVozidla.Add( self.LabelKPV_k1lehotaTKstazPodm, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.LabelHV_TH = wx.StaticText( self.PageHodnotaVozidla, wx.ID_ANY, u"Technická hodnota vozidla (TH)=VHV.TSV/100+VHVM.TSVM/100:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelHV_TH.Wrap( -1 )

		GbSizerPageHodnotaVozidla.Add( self.LabelHV_TH, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 2 )

		self.TextBoxHV_TH = wx.TextCtrl( self.PageHodnotaVozidla, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxHV_TH" )
		GbSizerPageHodnotaVozidla.Add( self.TextBoxHV_TH, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 2 )

		self.LabelKPV_k1lehotaTKsuStazPodm = wx.StaticText( self.PageHodnotaVozidla, wx.ID_ANY, u"LabelKPV_k1lehotaTKsuStazPodm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPV_k1lehotaTKsuStazPodm.Wrap( -1 )

		self.LabelKPV_k1lehotaTKsuStazPodm.Hide()

		GbSizerPageHodnotaVozidla.Add( self.LabelKPV_k1lehotaTKsuStazPodm, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.LabelHV_VSH = wx.StaticText( self.PageHodnotaVozidla, wx.ID_ANY, u"Všeobecná hodnota vozidla (VŠH) = TH.kp:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelHV_VSH.Wrap( -1 )

		GbSizerPageHodnotaVozidla.Add( self.LabelHV_VSH, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 2 )

		self.TextBoxHV_VSH = wx.TextCtrl( self.PageHodnotaVozidla, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxHV_VSH" )
		GbSizerPageHodnotaVozidla.Add( self.TextBoxHV_VSH, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 2 )

		FrameKPV = wx.StaticBoxSizer( wx.StaticBox( self.PageHodnotaVozidla, wx.ID_ANY, u"Koeficient predajnosti vozidla" ), wx.VERTICAL )

		GbSizerFrameKPV = wx.GridBagSizer( 0, 0 )
		GbSizerFrameKPV.SetFlexibleDirection( wx.BOTH )
		GbSizerFrameKPV.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.LabelKPV_K1 = wx.StaticText( FrameKPV.GetStaticBox(), wx.ID_ANY, u"platnosť kontroly technického stavu vozidla (k1):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPV_K1.Wrap( -1 )

		GbSizerFrameKPV.Add( self.LabelKPV_K1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 2 )

		self.TextBoxKPV_K1 = wx.TextCtrl( FrameKPV.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K1" )
		GbSizerFrameKPV.Add( self.TextBoxKPV_K1, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 2 )

		self.LabelKPV_koniecTK = wx.StaticText( FrameKPV.GetStaticBox(), wx.ID_ANY, u"koniec platnosti TK:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPV_koniecTK.Wrap( -1 )

		GbSizerFrameKPV.Add( self.LabelKPV_koniecTK, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 2 )

		GbSizerTextBoxKPV_koniecTK = wx.GridBagSizer( 0, 0 )
		GbSizerTextBoxKPV_koniecTK.SetFlexibleDirection( wx.BOTH )
		GbSizerTextBoxKPV_koniecTK.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.TextBoxKPV_koniecTK = wx.TextCtrl( FrameKPV.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0, wx.DefaultValidator, u"TextBoxKPV_koniecTK" )
		GbSizerTextBoxKPV_koniecTK.Add( self.TextBoxKPV_koniecTK, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.LEFT, 2 )

		self.DatePickerTextBoxKPV_koniecTK = wx.adv.DatePickerCtrl( FrameKPV.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 20,-1 ), wx.adv.DP_DROPDOWN )
		GbSizerTextBoxKPV_koniecTK.Add( self.DatePickerTextBoxKPV_koniecTK, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT, 2 )


		GbSizerFrameKPV.Add( GbSizerTextBoxKPV_koniecTK, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.LabelKVP_poskodenie = wx.StaticText( FrameKPV.GetStaticBox(), wx.ID_ANY, u"poškodenie vozidla haváriou (k2):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKVP_poskodenie.Wrap( -1 )

		GbSizerFrameKPV.Add( self.LabelKVP_poskodenie, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 2 )

		self.TextBoxKPV_K2 = wx.TextCtrl( FrameKPV.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K2" )
		GbSizerFrameKPV.Add( self.TextBoxKPV_K2, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )

		ComboBoxKPV_poskodenieChoices = []
		self.ComboBoxKPV_poskodenie = wx.Choice( FrameKPV.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), ComboBoxKPV_poskodenieChoices, 0, wx.DefaultValidator, u"ComboBoxKPV_poskodenie" )
		self.ComboBoxKPV_poskodenie.SetSelection( 0 )
		self.ComboBoxKPV_poskodenie.SetMaxSize( wx.Size( 400,-1 ) )

		GbSizerFrameKPV.Add( self.ComboBoxKPV_poskodenie, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 2 )

		self.LabelKVP_pocetDrzitelov = wx.StaticText( FrameKPV.GetStaticBox(), wx.ID_ANY, u"počet držiteľov vozidla (k3):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKVP_pocetDrzitelov.Wrap( -1 )

		GbSizerFrameKPV.Add( self.LabelKVP_pocetDrzitelov, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 2 )

		self.TextBoxKPV_K3 = wx.TextCtrl( FrameKPV.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K3" )
		GbSizerFrameKPV.Add( self.TextBoxKPV_K3, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 2 )

		self.LabelKPV_PocetDrzitelov = wx.StaticText( FrameKPV.GetStaticBox(), wx.ID_ANY, u"súčasný držiteľ poradie:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPV_PocetDrzitelov.Wrap( -1 )

		GbSizerFrameKPV.Add( self.LabelKPV_PocetDrzitelov, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 2 )

		self.TextBoxKPVPocetDrzitelov = wx.SpinCtrl( FrameKPV.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 100, 0, u"TextBoxKPVPocetDrzitelov" )
		GbSizerFrameKPV.Add( self.TextBoxKPVPocetDrzitelov, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.CheckBoxKPVk3Nezistene = wx.CheckBox( FrameKPV.GetStaticBox(), wx.ID_ANY, u"Nepreukázané", wx.DefaultPosition, wx.DefaultSize, 0 )
		GbSizerFrameKPV.Add( self.CheckBoxKPVk3Nezistene, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )

		self.LabelKPV_prevadzka = wx.StaticText( FrameKPV.GetStaticBox(), wx.ID_ANY, u"spôsob prevádzky vozidla (k4):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPV_prevadzka.Wrap( -1 )

		GbSizerFrameKPV.Add( self.LabelKPV_prevadzka, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 2 )

		self.TextBoxKPV_K4 = wx.TextCtrl( FrameKPV.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K4" )
		GbSizerFrameKPV.Add( self.TextBoxKPV_K4, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 2 )

		ComboBoxKPV_prevadzkaChoices = []
		self.ComboBoxKPV_prevadzka = wx.Choice( FrameKPV.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ComboBoxKPV_prevadzkaChoices, 0, wx.DefaultValidator, u"ComboBoxKPV_prevadzka" )
		self.ComboBoxKPV_prevadzka.SetSelection( 0 )
		GbSizerFrameKPV.Add( self.ComboBoxKPV_prevadzka, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 2 )

		self.LabelKPV_K5 = wx.StaticText( FrameKPV.GetStaticBox(), wx.ID_ANY, u"dopyt trhu (k5):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPV_K5.Wrap( -1 )

		GbSizerFrameKPV.Add( self.LabelKPV_K5, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 2 )

		self.TextBoxKPV_K5 = wx.TextCtrl( FrameKPV.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5" )
		GbSizerFrameKPV.Add( self.TextBoxKPV_K5, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 2 )

		FrameHV_KK = wx.StaticBoxSizer( wx.StaticBox( FrameKPV.GetStaticBox(), wx.ID_ANY, u"Porovnateľné vozidlá" ), wx.VERTICAL )

		GbSizerFrameHV_KK = wx.GridBagSizer( 0, 0 )
		GbSizerFrameHV_KK.SetFlexibleDirection( wx.BOTH )
		GbSizerFrameHV_KK.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.LabelKPV_K5Zdroj = wx.StaticText( FrameHV_KK.GetStaticBox(), wx.ID_ANY, u"Zdroj", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.LabelKPV_K5Zdroj.Wrap( -1 )

		GbSizerFrameHV_KK.Add( self.LabelKPV_K5Zdroj, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		self.LabelKPV_K5VHV = wx.StaticText( FrameHV_KK.GetStaticBox(), wx.ID_ANY, u"VHV", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPV_K5VHV.Wrap( -1 )

		GbSizerFrameHV_KK.Add( self.LabelKPV_K5VHV, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 0 )

		self.LabelKPV_K5vPrevadzke = wx.StaticText( FrameHV_KK.GetStaticBox(), wx.ID_ANY, u"v prevadzke od", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPV_K5vPrevadzke.Wrap( -1 )

		GbSizerFrameHV_KK.Add( self.LabelKPV_K5vPrevadzke, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		self.LabelKPV_K5km = wx.StaticText( FrameHV_KK.GetStaticBox(), wx.ID_ANY, u"km", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPV_K5km.Wrap( -1 )

		GbSizerFrameHV_KK.Add( self.LabelKPV_K5km, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 0 )

		self.LabelKPV_K5Cena = wx.StaticText( FrameHV_KK.GetStaticBox(), wx.ID_ANY, u"Predajná cena", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPV_K5Cena.Wrap( -1 )

		GbSizerFrameHV_KK.Add( self.LabelKPV_K5Cena, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 0 )

		self.LabelKPV_K5TSV = wx.StaticText( FrameHV_KK.GetStaticBox(), wx.ID_ANY, u"TSV", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPV_K5TSV.Wrap( -1 )

		GbSizerFrameHV_KK.Add( self.LabelKPV_K5TSV, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 0 )

		self.LabelKPV_K5VHMV = wx.StaticText( FrameHV_KK.GetStaticBox(), wx.ID_ANY, u"VHMV", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPV_K5VHMV.Wrap( -1 )

		GbSizerFrameHV_KK.Add( self.LabelKPV_K5VHMV, wx.GBPosition( 0, 6 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		self.LabelKPV_K5TSMV = wx.StaticText( FrameHV_KK.GetStaticBox(), wx.ID_ANY, u"TSMV", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPV_K5TSMV.Wrap( -1 )

		GbSizerFrameHV_KK.Add( self.LabelKPV_K5TSMV, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		self.LabelKPV_K5TH = wx.StaticText( FrameHV_KK.GetStaticBox(), wx.ID_ANY, u"TH", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPV_K5TH.Wrap( -1 )

		GbSizerFrameHV_KK.Add( self.LabelKPV_K5TH, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 0 )

		self.TextBoxKPV_K5Zdroj1 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxKPV_K5Zdroj#1" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5Zdroj1, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5VHV1 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5VHV#1" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5VHV1, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5vPrevadzke1 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5vPrevadzke#1" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5vPrevadzke1, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5km1 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5km#1" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5km1, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5Cena1 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5Cena#1" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5Cena1, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5TSVedit1 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5TSV#1" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TSVedit1, wx.GBPosition( 1, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5TSV1 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 0,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"1" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TSV1, wx.GBPosition( 1, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxKPV_K5VHMV1 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5VHMV#1" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5VHMV1, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5TSMV1 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5TSMV#1" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TSMV1, wx.GBPosition( 1, 7 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5TH1 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5TH#1" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TH1, wx.GBPosition( 1, 8 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5Zdroj2 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxKPV_K5Zdroj#2" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5Zdroj2, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxKPV_K5VHV2 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5VHV#2" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5VHV2, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5vPrevadzke2 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5vPrevadzke#2" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5vPrevadzke2, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5km2 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5km#2" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5km2, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5Cena2 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5Cena#2" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5Cena2, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5TSVedit2 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5TSV#2" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TSVedit2, wx.GBPosition( 2, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5TSV2 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 0,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"2" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TSV2, wx.GBPosition( 2, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxKPV_K5VHMV2 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5VHMV#2" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5VHMV2, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5TSMV2 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5TSMV#2" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TSMV2, wx.GBPosition( 2, 7 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5TH2 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5TH#2" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TH2, wx.GBPosition( 2, 8 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5Zdroj3 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxKPV_K5Zdroj#3" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5Zdroj3, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxKPV_K5VHV3 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5VHV#3" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5VHV3, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5vPrevadzke3 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5vPrevadzke#3" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5vPrevadzke3, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5km3 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5km#3" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5km3, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5Cena3 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5Cena#3" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5Cena3, wx.GBPosition( 3, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5TSVedit3 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5TSV#3" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TSVedit3, wx.GBPosition( 3, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5TSV3 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 0,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"3" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TSV3, wx.GBPosition( 3, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxKPV_K5VHMV3 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5VHMV#3" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5VHMV3, wx.GBPosition( 3, 6 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5TSMV3 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5TSMV#3" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TSMV3, wx.GBPosition( 3, 7 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5TH3 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5TH#3" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TH3, wx.GBPosition( 3, 8 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5Zdroj4 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxKPV_K5Zdroj#4" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5Zdroj4, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxKPV_K5VHV4 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5VHV#4" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5VHV4, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5vPrevadzke4 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5vPrevadzke#4" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5vPrevadzke4, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5km4 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5km#4" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5km4, wx.GBPosition( 4, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5Cena4 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5Cena#4" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5Cena4, wx.GBPosition( 4, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5TSVedit4 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5TSV#4" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TSVedit4, wx.GBPosition( 4, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5TSV4 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 0,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"4" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TSV4, wx.GBPosition( 4, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxKPV_K5VHMV4 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5VHMV#4" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5VHMV4, wx.GBPosition( 4, 6 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5TSMV4 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5TSMV#4" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TSMV4, wx.GBPosition( 4, 7 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5TH4 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5TH#4" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TH4, wx.GBPosition( 4, 8 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5Zdroj5 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"TextBoxKPV_K5Zdroj#5" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5Zdroj5, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxKPV_K5VHV5 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5VHV#5" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5VHV5, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5vPrevadzke5 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5vPrevadzke#5" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5vPrevadzke5, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5km5 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5km#5" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5km5, wx.GBPosition( 5, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5Cena5 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5Cena#5" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5Cena5, wx.GBPosition( 5, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5TSVedit5 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5TSV#5" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TSVedit5, wx.GBPosition( 5, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxKPV_K5TSV5 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 0,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"4" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TSV5, wx.GBPosition( 5, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

		self.TextBoxKPV_K5VHMV5 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5VHMV#5" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5VHMV5, wx.GBPosition( 5, 6 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5TSMV5 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5TSMV#5" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TSMV5, wx.GBPosition( 5, 7 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.TextBoxKPV_K5TH5 = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_K5TH#5" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPV_K5TH5, wx.GBPosition( 5, 8 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.LabelKPV_priemPredajCena = wx.StaticText( FrameHV_KK.GetStaticBox(), wx.ID_ANY, u"priemerná predajná cena:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPV_priemPredajCena.Wrap( -1 )

		GbSizerFrameHV_KK.Add( self.LabelKPV_priemPredajCena, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 0 )

		self.TextBoxKPVpriemPredajCena = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPVpriemPredajCena" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPVpriemPredajCena, wx.GBPosition( 6, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 0 )

		self.LabelKPVpriemTechHednVozidla = wx.StaticText( FrameHV_KK.GetStaticBox(), wx.ID_ANY, u"priemerná TH vozidiel:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKPVpriemTechHednVozidla.Wrap( -1 )

		GbSizerFrameHV_KK.Add( self.LabelKPVpriemTechHednVozidla, wx.GBPosition( 6, 5 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0 )

		self.TextBoxKPVpriemTechHodnVozidla = wx.TextCtrl( FrameHV_KK.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPVpriemTechHodnVozidla" )
		GbSizerFrameHV_KK.Add( self.TextBoxKPVpriemTechHodnVozidla, wx.GBPosition( 6, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )


		FrameHV_KK.Add( GbSizerFrameHV_KK, 1, wx.EXPAND, 0 )


		GbSizerFrameKPV.Add( FrameHV_KK, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 5 ), wx.EXPAND, 0 )

		self.LabelKVP_koeficientPredajnost = wx.StaticText( FrameKPV.GetStaticBox(), wx.ID_ANY, u"Koeficient predajnosti vozidla (kp)=k1.k2.k3.k4.k5:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelKVP_koeficientPredajnost.Wrap( -1 )

		GbSizerFrameKPV.Add( self.LabelKVP_koeficientPredajnost, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 2 )

		self.TextBoxKPV_Kp = wx.TextCtrl( FrameKPV.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT, wx.DefaultValidator, u"TextBoxKPV_Kp" )
		GbSizerFrameKPV.Add( self.TextBoxKPV_Kp, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 2 )


		FrameKPV.Add( GbSizerFrameKPV, 1, wx.EXPAND, 5 )


		GbSizerPageHodnotaVozidla.Add( FrameKPV, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 4 ), wx.EXPAND, 0 )


		self.PageHodnotaVozidla.SetSizer( GbSizerPageHodnotaVozidla )
		self.PageHodnotaVozidla.Layout()
		GbSizerPageHodnotaVozidla.Fit( self.PageHodnotaVozidla )
		self.MultiPageVDC.AddPage( self.PageHodnotaVozidla, u"Hodnota vozidla", False )
		self.PageNakladyNaOpravu = wx.Panel( self.MultiPageVDC, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.PageNakladyNaOpravu.Enable( False )

		self.MultiPageVDC.AddPage( self.PageNakladyNaOpravu, u"Náklady na opravu", False )
		self.PageZnehodnotenie = wx.Panel( self.MultiPageVDC, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.PageZnehodnotenie.Hide()

		self.MultiPageVDC.AddPage( self.PageZnehodnotenie, u"Znehodnotenie", False )

		mainGbSizer.Add( self.MultiPageVDC, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 7 ), wx.EXPAND |wx.ALL, 5 )

		self.TextBoxInformacia = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		mainGbSizer.Add( self.TextBoxInformacia, wx.GBPosition( 2, 0 ), wx.GBSpan( 6, 7 ), wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( mainGbSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.ButtonNovyVypocet.Bind( wx.EVT_BUTTON, self.NovyVypocet )
		self.ButtonNovyVypocet.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.ButtonOtvoritFromFile.Bind( wx.EVT_BUTTON, self.OtvorZoSuboru )
		self.ButtonOtvoritFromFile.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.ButtonUlozitToFile.Bind( wx.EVT_BUTTON, self.ButtonUlozitToFileOnButtonClick )
		self.ButtonUlozitToFile.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.ButtonOtvoritZdb.Bind( wx.EVT_BUTTON, self.ButtonOtvoritZdbOnButtonClick )
		self.ButtonOtvoritZdb.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.ButtonUlozitDOdb.Bind( wx.EVT_BUTTON, self.ButtonUlozitDOdbOnButtonClick )
		self.ButtonUlozitDOdb.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.ButtonNNO_Tlac.Bind( wx.EVT_BUTTON, self.ButtonNNO_TlacOnButtonClick )
		self.ButtonNNO_Tlac.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.ButtonTest.Bind( wx.EVT_BUTTON, self.ButtonTestOnButtonClick )
		self.TextBoxCisloPripadu.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxCPU.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.DateTimePickerDatumPU.Bind( wx.adv.EVT_DATE_CHANGED, self.DateTimePickerDatumPUOnDateChanged )
		self.TextBoxDatumPU.Bind( wx.EVT_KILL_FOCUS, self.TextBoxDatumPUOnKillFocus )
		self.TextBoxDatumPU.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPoskodeny.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.CheckBoxPlatcaDPH.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPoskodenyAdresa.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxUzivatelVytvoril.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxDatumVytvorenia.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxUzivatelZmenil.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxDatumZmeny.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPoznamka.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxECV.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPrideleneECV.Bind( wx.EVT_KILL_FOCUS, self.TextBoxPrideleneECVOnKillFocus )
		self.TextBoxPrideleneECV.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.DateTimePickerPrideleneECV.Bind( wx.adv.EVT_DATE_CHANGED, self.DateTimePickerPrideleneECVOnDateChanged )
		self.ComboBoxKategoriaMV.Bind( wx.EVT_CHOICE, self.ComboBoxKategoriaMVOnChoice )
		self.ComboBoxKategoriaMV.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.ComboBoxPodkategoriaMV.Bind( wx.EVT_CHOICE, self.ComboBoxPodkategoriaMVOnChoice )
		self.ComboBoxPodkategoriaMV.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxZnackaMV.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxVIN.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxCisloTP.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxObjemMotora.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxVykon.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxOtacky.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxCisloMotora.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxCisloRamu.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.ComboBoxPalivo.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxHmotnostCelkova.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPohotovostnaHmotnost.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPocetNaprav.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxCelkovaDlzka.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxRazvor.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPocetDveri.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxOdjazdene.Bind( wx.EVT_KILL_FOCUS, self.TextBoxOdjazdeneOnKillFocus )
		self.TextBoxOdjazdene.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxFarba.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxRokVyrobyMV.Bind( wx.EVT_KILL_FOCUS, self.TextBoxRokVyrobyMVOnKillFocus )
		self.TextBoxRokVyrobyMV.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxVprevadzkeOd.Bind( wx.EVT_KILL_FOCUS, self.TextBoxVprevadzkeOdOnKillFocus )
		self.TextBoxVprevadzkeOd.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.DateTimePickerVprevadzkeOd.Bind( wx.adv.EVT_DATE_CHANGED, self.DateTimePickerVprevadzkeOdOnDateChanged )
		self.TextBoxDobaPrevadzkyMesiac.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPneuPocet1.Bind( wx.EVT_KILL_FOCUS, self.TextBoxPneuPocetOnKillFocus )
		self.TextBoxPneuPocet1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPneuPopis1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPneuPriamaTH1.Bind( wx.EVT_KILL_FOCUS, self.TextBoxPneuPriamaTHOnKillFocus )
		self.TextBoxPneuPriamaTH1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPneuNamerane1.Bind( wx.EVT_KILL_FOCUS, self.TextBoxPneuMMOnKillFocus )
		self.TextBoxPneuNamerane1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPneuNove1.Bind( wx.EVT_KILL_FOCUS, self.TextBoxPneuMMOnKillFocus )
		self.TextBoxPneuNove1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPneuTH1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPneuPocet2.Bind( wx.EVT_KILL_FOCUS, self.TextBoxPneuPocetOnKillFocus )
		self.TextBoxPneuPocet2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPneuPopis2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPneuPriamaTH2.Bind( wx.EVT_KILL_FOCUS, self.TextBoxPneuPriamaTHOnKillFocus )
		self.TextBoxPneuPriamaTH2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPneuNamerane2.Bind( wx.EVT_KILL_FOCUS, self.TextBoxPneuMMOnKillFocus )
		self.TextBoxPneuNamerane2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPneuNove2.Bind( wx.EVT_KILL_FOCUS, self.TextBoxPneuMMOnKillFocus )
		self.TextBoxPneuNove2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPneuTH2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPneuPocet3.Bind( wx.EVT_KILL_FOCUS, self.TextBoxPneuPocetOnKillFocus )
		self.TextBoxPneuPocet3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPneuPopis3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPneuPriamaTH3.Bind( wx.EVT_KILL_FOCUS, self.TextBoxPneuPriamaTHOnKillFocus )
		self.TextBoxPneuPriamaTH3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPneuNamerane3.Bind( wx.EVT_KILL_FOCUS, self.TextBoxPneuMMOnKillFocus )
		self.TextBoxPneuNamerane3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPneuNove3.Bind( wx.EVT_KILL_FOCUS, self.TextBoxPneuMMOnKillFocus )
		self.TextBoxPneuNove3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPneuTH3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxPneuTH.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHdobaPrevadzky.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPKV.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPZTS.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPEZ.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPRKM.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHRKM.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHkKM.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHkAM.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.ComboBoxTHRozdelitSkupiny.Bind( wx.EVT_CHOICE, self.ComboBoxTHRozdelitSkupinyOnChoice )
		self.ComboBoxTHRozdelitSkupiny.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHSkupina1.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHSkupinaOnKillFocus )
		self.TextBoxTHSkupina1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHVTSS1.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHVTSSOnKillFocus )
		self.TextBoxTHVTSS1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPDS1.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHPDSOnKillFocus )
		self.TextBoxTHPDS1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZAV1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZA1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZP1.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHZPOnKillFocus )
		self.TextBoxTHZP1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHTSS1edit.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHTSSeditOnKillFocus )
		self.TextBoxTHTSS1edit.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPTSS1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHSkupina2.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHSkupinaOnKillFocus )
		self.TextBoxTHSkupina2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHVTSS2.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHVTSSOnKillFocus )
		self.TextBoxTHVTSS2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPDS2.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHPDSOnKillFocus )
		self.TextBoxTHPDS2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZAV2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZA2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZP2.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHZPOnKillFocus )
		self.TextBoxTHZP2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHTSS2edit.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHTSSeditOnKillFocus )
		self.TextBoxTHTSS2edit.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPTSS2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHSkupina3.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHSkupinaOnKillFocus )
		self.TextBoxTHSkupina3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHVTSS3.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHVTSSOnKillFocus )
		self.TextBoxTHVTSS3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPDS3.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHPDSOnKillFocus )
		self.TextBoxTHPDS3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZAV3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZA3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZP3.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHZPOnKillFocus )
		self.TextBoxTHZP3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHTSS3edit.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHTSSeditOnKillFocus )
		self.TextBoxTHTSS3edit.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPTSS3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHSkupina4.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHSkupinaOnKillFocus )
		self.TextBoxTHSkupina4.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHVTSS4.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHVTSSOnKillFocus )
		self.TextBoxTHVTSS4.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPDS4.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHPDSOnKillFocus )
		self.TextBoxTHPDS4.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZAV4.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZA4.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZP4.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHZPOnKillFocus )
		self.TextBoxTHZP4.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHTSS4edit.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHTSSeditOnKillFocus )
		self.TextBoxTHTSS4edit.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPTSS4.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHSkupina5.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHSkupinaOnKillFocus )
		self.TextBoxTHSkupina5.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHVTSS5.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHVTSSOnKillFocus )
		self.TextBoxTHVTSS5.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPDS5.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHPDSOnKillFocus )
		self.TextBoxTHPDS5.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZAV5.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZA5.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZP5.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHZPOnKillFocus )
		self.TextBoxTHZP5.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHTSS5edit.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHTSSeditOnKillFocus )
		self.TextBoxTHTSS5edit.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPTSS5.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHSkupina6.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHSkupinaOnKillFocus )
		self.TextBoxTHSkupina6.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHVTSS6.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHVTSSOnKillFocus )
		self.TextBoxTHVTSS6.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPDS6.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHPDSOnKillFocus )
		self.TextBoxTHPDS6.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZAV6.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZA6.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZP6.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHZPOnKillFocus )
		self.TextBoxTHZP6.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHTSS6edit.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHTSSeditOnKillFocus )
		self.TextBoxTHTSS6edit.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPTSS6.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHSkupina7.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHSkupinaOnKillFocus )
		self.TextBoxTHSkupina7.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHVTSS7.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHVTSSOnKillFocus )
		self.TextBoxTHVTSS7.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPDS7.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHPDSOnKillFocus )
		self.TextBoxTHPDS7.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZAV7.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZA7.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZP7.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHZPOnKillFocus )
		self.TextBoxTHZP7.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHTSS7edit.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHTSSeditOnKillFocus )
		self.TextBoxTHTSS7edit.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPTSS7.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHSkupina8.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHSkupinaOnKillFocus )
		self.TextBoxTHSkupina8.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHVTSS8.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHVTSSOnKillFocus )
		self.TextBoxTHVTSS8.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPDS8.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHPDSOnKillFocus )
		self.TextBoxTHPDS8.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZAV8.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZA8.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZP8.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHZPOnKillFocus )
		self.TextBoxTHZP8.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHTSS8edit.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHTSSeditOnKillFocus )
		self.TextBoxTHTSS8edit.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPTSS8.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHSkupina9.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHSkupinaOnKillFocus )
		self.TextBoxTHSkupina9.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHVTSS9.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHVTSSOnKillFocus )
		self.TextBoxTHVTSS9.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPDS9.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHPDSOnKillFocus )
		self.TextBoxTHPDS9.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZAV9.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZA9.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHZP9.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHZPOnKillFocus )
		self.TextBoxTHZP9.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHTSS9edit.Bind( wx.EVT_KILL_FOCUS, self.TextBoxTHTSSeditOnKillFocus )
		self.TextBoxTHTSS9edit.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPTSS9.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHPDSSpolu.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxTHTSV.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxHV_VHV.Bind( wx.EVT_KILL_FOCUS, self.TextBoxHV_VHVOnKillFocus )
		self.TextBoxHV_VHV.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxHV_TSV.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxHV_VHMV.Bind( wx.EVT_KILL_FOCUS, self.TextBoxHV_VHVOnKillFocus )
		self.TextBoxHV_VHMV.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxHV_TSMV.Bind( wx.EVT_KILL_FOCUS, self.TextBoxHV_TSMVOnKillFocus )
		self.TextBoxHV_TSMV.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxHV_TH.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxHV_VSH.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_koniecTK.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_koniecTKOnKillFocus )
		self.TextBoxKPV_koniecTK.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.DatePickerTextBoxKPV_koniecTK.Bind( wx.adv.EVT_DATE_CHANGED, self.DatePickerTextBoxKPV_koniecTKOnDateChanged )
		self.TextBoxKPV_K2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.ComboBoxKPV_poskodenie.Bind( wx.EVT_CHOICE, self.ComboBoxKPV_poskodenieOnChoice )
		self.ComboBoxKPV_poskodenie.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPVPocetDrzitelov.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPVPocetDrzitelov.Bind( wx.EVT_SPINCTRL, self.TextBoxKPVPocetDrzitelovOnSpinCtrl )
		self.CheckBoxKPVk3Nezistene.Bind( wx.EVT_CHECKBOX, self.CheckBoxKPVk3NezisteneOnCheckBox )
		self.TextBoxKPV_K4.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.ComboBoxKPV_prevadzka.Bind( wx.EVT_CHOICE, self.ComboBoxKPV_prevadzkaOnChoice )
		self.ComboBoxKPV_prevadzka.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5OnKillFocus )
		self.TextBoxKPV_K5.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5Zdroj1.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5ZdrojOnKillFocus )
		self.TextBoxKPV_K5Zdroj1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5VHV1.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5VHVOnKillFocus )
		self.TextBoxKPV_K5VHV1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5vPrevadzke1.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5vPrevadzkeOnKillFocus )
		self.TextBoxKPV_K5vPrevadzke1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5km1.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5kmOnKillFocus )
		self.TextBoxKPV_K5km1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5Cena1.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5CenaOnKillFocus )
		self.TextBoxKPV_K5Cena1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TSVedit1.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5TSVeditOnKillFocus )
		self.TextBoxKPV_K5TSVedit1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TSV1.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5TSVeditOnKillFocus )
		self.TextBoxKPV_K5VHMV1.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5VHMVOnKillFocus )
		self.TextBoxKPV_K5VHMV1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TSMV1.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5TSMVOnKillFocus )
		self.TextBoxKPV_K5TSMV1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TH1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5Zdroj2.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5ZdrojOnKillFocus )
		self.TextBoxKPV_K5Zdroj2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5VHV2.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5VHVOnKillFocus )
		self.TextBoxKPV_K5VHV2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5vPrevadzke2.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5vPrevadzkeOnKillFocus )
		self.TextBoxKPV_K5vPrevadzke2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5km2.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5kmOnKillFocus )
		self.TextBoxKPV_K5km2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5Cena2.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5CenaOnKillFocus )
		self.TextBoxKPV_K5Cena2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TSVedit2.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5TSVeditOnKillFocus )
		self.TextBoxKPV_K5TSVedit2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TSV2.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5TSVeditOnKillFocus )
		self.TextBoxKPV_K5VHMV2.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5VHMVOnKillFocus )
		self.TextBoxKPV_K5VHMV2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TSMV2.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5TSMVOnKillFocus )
		self.TextBoxKPV_K5TSMV2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TH2.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5Zdroj3.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5ZdrojOnKillFocus )
		self.TextBoxKPV_K5Zdroj3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5VHV3.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5VHVOnKillFocus )
		self.TextBoxKPV_K5VHV3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5vPrevadzke3.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5vPrevadzkeOnKillFocus )
		self.TextBoxKPV_K5vPrevadzke3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5km3.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5kmOnKillFocus )
		self.TextBoxKPV_K5km3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5Cena3.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5CenaOnKillFocus )
		self.TextBoxKPV_K5Cena3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TSVedit3.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5TSVeditOnKillFocus )
		self.TextBoxKPV_K5TSVedit3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TSV3.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5TSVeditOnKillFocus )
		self.TextBoxKPV_K5VHMV3.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5VHMVOnKillFocus )
		self.TextBoxKPV_K5VHMV3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TSMV3.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5TSMVOnKillFocus )
		self.TextBoxKPV_K5TSMV3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TH3.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5Zdroj4.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5ZdrojOnKillFocus )
		self.TextBoxKPV_K5Zdroj4.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5VHV4.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5VHVOnKillFocus )
		self.TextBoxKPV_K5VHV4.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5vPrevadzke4.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5vPrevadzkeOnKillFocus )
		self.TextBoxKPV_K5vPrevadzke4.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5km4.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5kmOnKillFocus )
		self.TextBoxKPV_K5km4.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5Cena4.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5CenaOnKillFocus )
		self.TextBoxKPV_K5Cena4.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TSVedit4.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5TSVeditOnKillFocus )
		self.TextBoxKPV_K5TSVedit4.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TSV4.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5TSVeditOnKillFocus )
		self.TextBoxKPV_K5VHMV4.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5VHMVOnKillFocus )
		self.TextBoxKPV_K5VHMV4.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TSMV4.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5TSMVOnKillFocus )
		self.TextBoxKPV_K5TSMV4.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TH4.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5Zdroj5.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5ZdrojOnKillFocus )
		self.TextBoxKPV_K5Zdroj5.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5VHV5.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5VHVOnKillFocus )
		self.TextBoxKPV_K5VHV5.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5vPrevadzke5.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5vPrevadzkeOnKillFocus )
		self.TextBoxKPV_K5vPrevadzke5.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5km5.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5kmOnKillFocus )
		self.TextBoxKPV_K5km5.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5Cena5.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5CenaOnKillFocus )
		self.TextBoxKPV_K5Cena5.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TSVedit5.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5TSVeditOnKillFocus )
		self.TextBoxKPV_K5TSVedit5.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TSV5.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5TSVeditOnKillFocus )
		self.TextBoxKPV_K5VHMV5.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5VHMVOnKillFocus )
		self.TextBoxKPV_K5VHMV5.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TSMV5.Bind( wx.EVT_KILL_FOCUS, self.TextBoxKPV_K5TSMVOnKillFocus )
		self.TextBoxKPV_K5TSMV5.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_K5TH5.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPVpriemPredajCena.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPVpriemTechHodnVozidla.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.TextBoxKPV_Kp.Bind( wx.EVT_SET_FOCUS, self.SetFocus )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def NovyVypocet( self, event ):
		pass

	def SetFocus( self, event ):
		pass

	def OtvorZoSuboru( self, event ):
		pass


	def ButtonUlozitToFileOnButtonClick( self, event ):
		pass


	def ButtonOtvoritZdbOnButtonClick( self, event ):
		pass


	def ButtonUlozitDOdbOnButtonClick( self, event ):
		pass


	def ButtonNNO_TlacOnButtonClick( self, event ):
		pass


	def ButtonTestOnButtonClick( self, event ):
		pass



	def DateTimePickerDatumPUOnDateChanged( self, event ):
		pass

	def TextBoxDatumPUOnKillFocus( self, event ):
		pass











	def TextBoxPrideleneECVOnKillFocus( self, event ):
		pass


	def DateTimePickerPrideleneECVOnDateChanged( self, event ):
		pass

	def ComboBoxKategoriaMVOnChoice( self, event ):
		pass


	def ComboBoxPodkategoriaMVOnChoice( self, event ):
		pass

















	def TextBoxOdjazdeneOnKillFocus( self, event ):
		pass



	def TextBoxRokVyrobyMVOnKillFocus( self, event ):
		pass


	def TextBoxVprevadzkeOdOnKillFocus( self, event ):
		pass


	def DateTimePickerVprevadzkeOdOnDateChanged( self, event ):
		pass


	def TextBoxPneuPocetOnKillFocus( self, event ):
		pass



	def TextBoxPneuPriamaTHOnKillFocus( self, event ):
		pass


	def TextBoxPneuMMOnKillFocus( self, event ):
		pass


































	def ComboBoxTHRozdelitSkupinyOnChoice( self, event ):
		pass


	def TextBoxTHSkupinaOnKillFocus( self, event ):
		pass


	def TextBoxTHVTSSOnKillFocus( self, event ):
		pass


	def TextBoxTHPDSOnKillFocus( self, event ):
		pass




	def TextBoxTHZPOnKillFocus( self, event ):
		pass


	def TextBoxTHTSSeditOnKillFocus( self, event ):
		pass













































































































	def TextBoxHV_VHVOnKillFocus( self, event ):
		pass





	def TextBoxHV_TSMVOnKillFocus( self, event ):
		pass





	def TextBoxKPV_koniecTKOnKillFocus( self, event ):
		pass


	def DatePickerTextBoxKPV_koniecTKOnDateChanged( self, event ):
		pass


	def ComboBoxKPV_poskodenieOnChoice( self, event ):
		pass




	def TextBoxKPVPocetDrzitelovOnSpinCtrl( self, event ):
		pass

	def CheckBoxKPVk3NezisteneOnCheckBox( self, event ):
		pass


	def ComboBoxKPV_prevadzkaOnChoice( self, event ):
		pass


	def TextBoxKPV_K5OnKillFocus( self, event ):
		pass


	def TextBoxKPV_K5ZdrojOnKillFocus( self, event ):
		pass


	def TextBoxKPV_K5VHVOnKillFocus( self, event ):
		pass


	def TextBoxKPV_K5vPrevadzkeOnKillFocus( self, event ):
		pass


	def TextBoxKPV_K5kmOnKillFocus( self, event ):
		pass


	def TextBoxKPV_K5CenaOnKillFocus( self, event ):
		pass


	def TextBoxKPV_K5TSVeditOnKillFocus( self, event ):
		pass



	def TextBoxKPV_K5VHMVOnKillFocus( self, event ):
		pass


	def TextBoxKPV_K5TSMVOnKillFocus( self, event ):
		pass















































































###########################################################################
## Class VDCdb
###########################################################################

class VDCdb ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Otvoriť z databázy", pos = wx.DefaultPosition, size = wx.Size( 682,320 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		GbSizerOpenDB = wx.GridBagSizer( 0, 0 )
		GbSizerOpenDB.SetFlexibleDirection( wx.BOTH )
		GbSizerOpenDB.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.LabelVyhladavanieID = wx.StaticText( self, wx.ID_ANY, u"ID VDC:", wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT )
		self.LabelVyhladavanieID.Wrap( -1 )

		GbSizerOpenDB.Add( self.LabelVyhladavanieID, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.TextBoxVyhladavanieID = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		GbSizerOpenDB.Add( self.TextBoxVyhladavanieID, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.LabelVyhladavanieCPU = wx.StaticText( self, wx.ID_ANY, u"Číslo PU:", wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT )
		self.LabelVyhladavanieCPU.Wrap( -1 )

		GbSizerOpenDB.Add( self.LabelVyhladavanieCPU, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.TextBoxVyhladavanieCisloPU = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		GbSizerOpenDB.Add( self.TextBoxVyhladavanieCisloPU, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.LabelVyhladavanieECV = wx.StaticText( self, wx.ID_ANY, u"EČV:", wx.DefaultPosition, wx.Size( 70,-1 ), wx.ALIGN_RIGHT )
		self.LabelVyhladavanieECV.Wrap( -1 )

		GbSizerOpenDB.Add( self.LabelVyhladavanieECV, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.TextBoxVyhladavanieECV = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		GbSizerOpenDB.Add( self.TextBoxVyhladavanieECV, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		gSizerTlacidla = wx.GridSizer( 0, 3, 0, 0 )

		self.ButtonVyhladat = wx.Button( self, wx.ID_ANY, u"Vyhladať", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		gSizerTlacidla.Add( self.ButtonVyhladat, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.ButtonNoveVyhladavanie = wx.Button( self, wx.ID_ANY, u"Nové vyhľadávanie", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		gSizerTlacidla.Add( self.ButtonNoveVyhladavanie, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.ButtonZobrazit = wx.Button( self, wx.ID_ANY, u"Zobraziť", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		gSizerTlacidla.Add( self.ButtonZobrazit, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		GbSizerOpenDB.Add( gSizerTlacidla, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 7 ), wx.EXPAND, 5 )

		self.GridVysledkyVyhladavania = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 650,200 ), 0 )

		# Grid
		self.GridVysledkyVyhladavania.CreateGrid( 0, 5 )
		self.GridVysledkyVyhladavania.EnableEditing( False )
		self.GridVysledkyVyhladavania.EnableGridLines( True )
		self.GridVysledkyVyhladavania.EnableDragGridSize( False )
		self.GridVysledkyVyhladavania.SetMargins( 0, 0 )

		# Columns
		self.GridVysledkyVyhladavania.SetColSize( 0, 30 )
		self.GridVysledkyVyhladavania.SetColSize( 1, 100 )
		self.GridVysledkyVyhladavania.SetColSize( 2, 100 )
		self.GridVysledkyVyhladavania.SetColSize( 3, 200 )
		self.GridVysledkyVyhladavania.SetColSize( 4, 200 )
		self.GridVysledkyVyhladavania.EnableDragColMove( False )
		self.GridVysledkyVyhladavania.EnableDragColSize( True )
		self.GridVysledkyVyhladavania.SetColLabelSize( 20 )
		self.GridVysledkyVyhladavania.SetColLabelValue( 0, u"ID" )
		self.GridVysledkyVyhladavania.SetColLabelValue( 1, u"CPU" )
		self.GridVysledkyVyhladavania.SetColLabelValue( 2, u"ECV" )
		self.GridVysledkyVyhladavania.SetColLabelValue( 3, u"Dátum vytvorenia" )
		self.GridVysledkyVyhladavania.SetColLabelValue( 4, u"Dátum zmeny" )
		self.GridVysledkyVyhladavania.SetColLabelValue( 5, wx.EmptyString )
		self.GridVysledkyVyhladavania.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.GridVysledkyVyhladavania.AutoSizeRows()
		self.GridVysledkyVyhladavania.EnableDragRowSize( True )
		self.GridVysledkyVyhladavania.SetRowLabelSize( 0 )
		self.GridVysledkyVyhladavania.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.GridVysledkyVyhladavania.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		GbSizerOpenDB.Add( self.GridVysledkyVyhladavania, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 8 ), wx.ALL, 5 )


		self.SetSizer( GbSizerOpenDB )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.ButtonVyhladat.Bind( wx.EVT_BUTTON, self.ButtonVyhladatOnButtonClick )
		self.ButtonNoveVyhladavanie.Bind( wx.EVT_BUTTON, self.ButtonNoveVyhladavanieOnButtonClick )
		self.ButtonZobrazit.Bind( wx.EVT_BUTTON, self.ButtonZobrazitOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ButtonVyhladatOnButtonClick( self, event ):
		pass

	def ButtonNoveVyhladavanieOnButtonClick( self, event ):
		pass

	def ButtonZobrazitOnButtonClick( self, event ):
		pass


