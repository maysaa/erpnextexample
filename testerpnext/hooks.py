# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "testerpnext"
app_title = "Testerpnext"
app_publisher = "KK"
app_description = "KK"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "KK"
app_license = "MIT"

web_include_css = "/assets/testerpnext/css/bootstrap.css"
web_include_css = "/assets/testerpnext/css/t.css"
web_include_js = "/assets/testerpnext/js/t.js"

app_include_css = "/assets/testerpnext/css/bootstrap.css"
app_include_css = "/assets/testerpnext/css/t.css"
app_include_js = "/assets/testerpnext/js/t.js"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/testerpnext/css/testerpnext.css"
# app_include_js = "/assets/testerpnext/js/testerpnext.js"

# include js, css files in header of web template
# web_include_css = "/assets/testerpnext/css/testerpnext.css"
# web_include_js = "/assets/testerpnext/js/testerpnext.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "testerpnext.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "testerpnext.install.before_install"
# after_install = "testerpnext.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "testerpnext.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"testerpnext.tasks.all"
# 	],
# 	"daily": [
# 		"testerpnext.tasks.daily"
# 	],
# 	"hourly": [
# 		"testerpnext.tasks.hourly"
# 	],
# 	"weekly": [
# 		"testerpnext.tasks.weekly"
# 	]
# 	"monthly": [
# 		"testerpnext.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "testerpnext.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "testerpnext.event.get_events"
# }

