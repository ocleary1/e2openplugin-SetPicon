# for localized messages  	 
from . import _
#
#  Set Picon - Plugin E2
#
#  by ims (c) 2012 ims21@users.sourceforge.net
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#

from Plugins.Plugin import PluginDescriptor
from Components.config import ConfigSubsection, config, ConfigYesNo

config.plugins.setpicon = ConfigSubsection()
config.plugins.setpicon.extmenu = ConfigYesNo(default=True)

def main(session, servicelist=None, **kwargs):
	global Servicelist
	Servicelist = servicelist
	global epg_bouquet
	epg_bouquet = Servicelist and Servicelist.getRoot()
	if epg_bouquet is not None:
		import ui
		from ServiceReference import ServiceReference
		services = ui.getBouquetServices(epg_bouquet)
		session.openWithCallback(ui.closed, ui.setPicon, plugin_path, services, ServiceReference(epg_bouquet).getServiceName())

def Plugins(path,**kwargs):
	global plugin_path
    	plugin_path = path
	name="SetPicon"
	descr=_("set picon to service")
	list = [ PluginDescriptor(name=name, description=descr, where=PluginDescriptor.WHERE_EVENTINFO, needsRestart = False, fnc=main),]
	if config.plugins.setpicon.extmenu.value:
		list.append(PluginDescriptor(name=name, description=descr, where=PluginDescriptor.WHERE_EXTENSIONSMENU, needsRestart = False, fnc=main))
	return list
