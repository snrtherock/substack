from substack.data.profile import Profile
from substack.helper.utils import LOG_PATH

profile = Profile()

profile.set_target("bkav.com")

# profile.set_enabled_plugins('search', ['BaiduPlugin', 'BingPlugin', 'GooglePlugin'])
profile.set_enabled_plugins('search', ['AskPlugin', 'YahooPlugin', 'BaiduPlugin', 'GooglePlugin'])
profile.set_enabled_plugins('dns', ['DNSPlugin'])
profile.set_enabled_plugins('port', ['NmapPlugin'])

http_settings = {
    "agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
    "proxy": ""
}

misc_settings = {
    "silent": False,
}

profile.set_http_settings(http_settings)
profile.set_misc_settings(misc_settings)
profile.set_name("empty_profile")
profile.set_desc("This is an empty profile that you can use to start a new configuration from.")

profile.save("empty")
#
# a = Profile("empty")
# print a.get_misc_settings()
# print a.get_http_settings("agent")
