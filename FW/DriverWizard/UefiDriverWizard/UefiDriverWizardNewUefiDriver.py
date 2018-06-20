## @file
# Subclass of NewUefiDriver, which is generated by wxFormBuilder.
#
# Copyright (c) 2012, Intel Corporation. All rights reserved.<BR>
#
# This program and the accompanying materials are licensed and made available
# under the terms and conditions of the BSD License which accompanies this
# distribution. The full text of the license may be found at
# http://opensource.org/licenses/bsd-license.php
#
# THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,
# WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.
#
##

"""Subclass of NewUefiDriver, which is generated by wxFormBuilder."""

##
# Import Modules
#
import Config
import wx
import os
import sys
import uuid
import string
import TemplateString
import UefiDriverWizard
import UefiDriverWizardNewPackage
import UefiDriverWizardNewUefiDriver
import UefiDriverWizardNewProtocol
import UefiDriverWizardNewGuid
import UefiDriverWizardNewLibraryClass
import UefiDriverWizardUefiDriverWizard
import UefiDriverWizardUefiDriverModelOptionalFeatures
import UefiDriverWizardUefiDriverModelConsumedProtocols
import UefiDriverWizardUefiDriverModelProducedProtocols

# Implementing NewUefiDriver
class UefiDriverWizardNewUefiDriver( UefiDriverWizard.NewUefiDriver ):
  def __init__( self, parent ):
    UefiDriverWizard.NewUefiDriver.__init__( self, parent )
    if Config.UefiDriverPath <> '':
      self.UefiDriverPath.SetPath(Config.UefiDriverPath + os.path.sep)
    else:
      if Config.PackagePath <> '':
        self.UefiDriverPath.SetPath(Config.PackagePath + os.path.sep)
      else:
        self.UefiDriverPath.SetPath(Config.WorkspacePath + os.path.sep)
    self.UefiDriverName.SetValue(Config.UefiDriverName)
    self.UefiDriverVersion.SetValue(Config.UefiDriverVersion)
    if Config.UefiDriverGuid == '':
      Config.UefiDriverGuid = uuid.uuid1().get_urn().split(':')[2]
    self.UefiDriverGuid.SetValue(Config.UefiDriverGuid)
    if Config.UefiDriverType == u"":
      Config.UefiDriverType = u"UEFI Driver Model Device Driver"
    self.UefiDriverType.SetStringSelection(Config.UefiDriverType)
    if Config.DriverBindingVersion == '':
      Config.DriverBindingVersion = '0x00000000'
    self.DriverBindingVersion.SetValue (Config.DriverBindingVersion)
    DriverModel = False
    if u"UEFI Driver Model Device Driver" in Config.UefiDriverType:
      DriverModel = True
    if u"UEFI Driver Model Bus Driver" in Config.UefiDriverType:
      DriverModel = True
    if u"UEFI Driver Model Hybrid Driver" in Config.UefiDriverType:
      DriverModel = True
    if DriverModel:
      self.DriverBindingVersion.Enable()
    else:
      self.DriverBindingVersion.Disable()
    if Config.UefiDriverCpuArchitecture == ():
      Config.UefiDriverCpuArchitecture = (u'All CPU Architectures',)
    self.UefiDriverCpuArchitecture.SetCheckedStrings(Config.UefiDriverCpuArchitecture)
    self.UefiDriverCommonFeatures.SetCheckedStrings(Config.UefiDriverCommonFeatures)
    if Config.UefiSpecificationVersion == '':
      Config.UefiSpecificationVersion = '0x0002001E'
    self.UefiSpecificationVersion.SetValue (Config.UefiSpecificationVersion)
    if u"Driver Supported EFI Version Protocol" in Config.UefiDriverCommonFeatures:
      self.UefiSpecificationVersion.Enable()
    else:
      self.UefiSpecificationVersion.Disable()
    if Config.Rfc4646LanguageCodes == '':
      Config.Rfc4646LanguageCodes = 'en'
    if Config.Iso639LanguageCodes == '':
      Config.Iso639LanguageCodes = 'eng'
    if Config.UefiDriverConsumedProtocols == ():
      Config.UefiDriverConsumedProtocols = (u"PCI Driver that consumes the PCI I/O Protocol",)
    if Config.UsbMajorVersion == '':
      Config.UsbMajorVersion = '3'
    if Config.UsbMinorVersion == '':
      Config.UsbMinorVersion = '0'

  # Handlers for NewUefiDriver events.
  def UefiDriverPathOnDirChanged( self, event ):
    if Config.UefiDriverName == '' or Config.UefiDriverName == os.path.split(Config.UefiDriverPath)[-1]:
      Config.UefiDriverPath = self.UefiDriverPath.GetPath()
      self.UefiDriverName.SetValue(os.path.split(Config.UefiDriverPath)[-1])
    else:
      Config.UefiDriverPath = self.UefiDriverPath.GetPath()

  def UefiDriverNameOnText( self, event ):
    Config.UefiDriverName = Config.App.TextFieldNameValid (self.UefiDriverName, event)

  def UefiDriverVersionOnText( self, event ):
    Config.UefiDriverVersion = Config.App.TextFieldVersionValid (self.UefiDriverVersion, event)

  def UefiDriverGuidOnText( self, event ):
    Config.UefiDriverGuid = event.GetString()

  def GenerateGuidOnButtonClick( self, event ):
    Config.UefiDriverGuid = uuid.uuid1().get_urn().split(':')[2]
    self.UefiDriverGuid.SetValue(Config.UefiDriverGuid)

  def UefiDriverTypeOnRadioBox( self, event ):
    Config.UefiDriverType = event.GetString()
    DriverModel = False
    if u"UEFI Driver Model Device Driver" in Config.UefiDriverType:
      DriverModel = True
    if u"UEFI Driver Model Bus Driver" in Config.UefiDriverType:
      DriverModel = True
    if u"UEFI Driver Model Hybrid Driver" in Config.UefiDriverType:
      DriverModel = True
    if DriverModel:
      self.DriverBindingVersion.Enable()
    else:
      self.DriverBindingVersion.Disable()

  def DriverBindingVersionOnText( self, event ):
    Config.DriverBindingVersion = event.GetString()

  def UefiDriverCommonFeaturesOnCheckListBoxToggled( self, event ):
    Config.UefiDriverCommonFeatures = self.UefiDriverCommonFeatures.GetCheckedStrings()
    if u"Driver Supported EFI Version Protocol" in Config.UefiDriverCommonFeatures:
      self.UefiSpecificationVersion.Enable()
    else:
      self.UefiSpecificationVersion.Disable()

  def UefiSpecificationVersionOnText( self, event ):
    Config.UefiSpecificationVersion = event.GetString()

  def UefiDriverCpuArchitectureOnCheckListBoxToggled( self, event ):
    if u'All CPU Architectures' in Config.UefiDriverCpuArchitecture:
      if len(self.UefiDriverCpuArchitecture.GetCheckedStrings()) <= 1:
        Config.UefiDriverCpuArchitecture = ()
      else:
        Config.UefiDriverCpuArchitecture = tuple(set(self.UefiDriverCpuArchitecture.GetCheckedStrings()) - set(Config.UefiDriverCpuArchitecture))
    else:
      if u'All CPU Architectures' in self.UefiDriverCpuArchitecture.GetCheckedStrings():
        Config.UefiDriverCpuArchitecture = ()
      else:
        Config.UefiDriverCpuArchitecture = self.UefiDriverCpuArchitecture.GetCheckedStrings()
    if len(Config.UefiDriverCpuArchitecture) == 0:
      Config.UefiDriverCpuArchitecture = (u'All CPU Architectures',)
    self.UefiDriverCpuArchitecture.SetCheckedStrings(Config.UefiDriverCpuArchitecture)

  def NextOnButtonClick( self, event ):
    self.Destroy()
    frame = UefiDriverWizardUefiDriverModelOptionalFeatures.UefiDriverWizardUefiDriverModelOptionalFeatures (None)
    frame.Show()

  def FinishOnButtonClick( self, event ):
    if Config.UefiDriverName == '':
      Config.UefiDriverName = os.path.split(Config.UefiDriverPath)[-1]
    Result, Message = Config.App.CreateUefiDriver()
    if not Result:
      dlg = wx.MessageDialog(
            self,
            Message,
            'ERROR',
            wx.OK | wx.ICON_ERROR
            )
      dlg.ShowModal()
      dlg.Destroy()
      return
    dlg = wx.MessageDialog(
          self,
          Message,
          'New UEFI Driver',
          wx.OK | wx.ICON_INFORMATION
          )
    dlg.ShowModal()
    dlg.Destroy()
    Config.UefiDriverName    = ''
    Config.UefiDriverVersion = ''
    Config.UefiDriverGuid    = ''
    self.Destroy()

  def CancelOnButtonClick( self, event ):
    Config.UefiDriverName    = ''
    Config.UefiDriverVersion = ''
    Config.UefiDriverGuid    = ''
    self.Destroy()