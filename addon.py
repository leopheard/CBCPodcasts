from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon
plugin = Plugin()
url1 = "https://www.cbc.ca/podcasting/includes/sks.xml" #Someone knows something
url2 = "https://www.cbc.ca/podcasting/includes/more.xml" #More with Anna Maria Tremonti
url3 = "https://www.cbc.ca/podcasting/includes/playme.xml" #PlayMe
url4 = "https://www.cbc.ca/podcasting/includes/current.xml" #TheCurrent
url5 = "https://www.cbc.ca/podcasting/includes/huntingwarhead.xml" #HuntingWarhead
url6 = "https://www.cbc.ca/podcasting/includes/frontburner.xml" #Frontburner
url7 = "https://www.cbc.ca/podcasting/includes/thepit.xml" #ThePit
url8 = "https://www.cbc.ca/podcasting/includes/sanctioned.xml" #Sanctioned:The Arrest of a Telecom Giant
url9 = "https://www.cbc.ca/podcasting/includes/secrets.xml" #Secrets Of the Fifth Estate
url10 = "https://www.cbc.ca/podcasting/includes/slumtown.xml" #Slumtown
url11 = "https://www.cbc.ca/podcasting/includes/spark.xml" #Spark
url12 = "https://www.cbc.ca/podcasting/includes/wiretap2020.xml" #Wiretap
url13 = "https://www.cbc.ca/podcasting/includes/worldonfire.xml" #WorldOnFire
url14 = "https://www.cbc.ca/podcasting/includes/thebandplayedon.xml" #BandPlayedOn
url15 = "https://podcasts.files.bbci.co.uk/b01mk3f8.rss" #ShortCuts
url16 = "https://www.cbc.ca/podcasting/includes/cf.xml" #ComedyFactory
url17 = "https://www.cbc.ca/podcasting/includes/atissue.xml" #NewsAtIssue
url18 = "https://rss.art19.com/guru" #Guru:TheDarkSideofEnlighenment
url19 = "https://www.cbc.ca/podcasting/includes/ambushed.xml" #Ambushed

@plugin.route('/')
def main_menu():
    items = [
#        {
#            'label': plugin.get_string(30000),
#            'path': "",
#            'thumbnail': "https://i.cbc.ca/1.4851944.1538750148!/fileImage/httpImage/image.png_gen/derivatives/16x9_780/cbc-podcasts.png", 
#            'is_playable': True},
        {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://www.cbc.ca/radio/podcasts/images/somoneknowssomething-promo.jpg"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://www.cbc.ca/radio/podcasts/images/promo-more-sm.jpg"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://www.cbc.ca/radio/podcasts/images/Promo_PlayMe-sm.jpg"},
        {
            'label': plugin.get_string(30004),
            'path': plugin.url_for('episodes4'),
            'thumbnail': "https://www.cbc.ca/radio/podcasts/images/promo-thecurrent-sm.jpg"},
        {
            'label': plugin.get_string(30005),
            'path': plugin.url_for('episodes5'),
            'thumbnail': "https://www.cbc.ca/radio/podcasts/images/promo-hunting-warhead-sm.jpg"},
        {
            'label': plugin.get_string(30006),
            'path': plugin.url_for('episodes6'),
            'thumbnail': "https://www.cbc.ca/radio/podcasts/images/950x950/frontburner-podcast-template.jpg"},
        {
            'label': plugin.get_string(30007),
            'path': plugin.url_for('episodes7'),
            'thumbnail': "https://www.cbc.ca/radio/podcasts/images/950x950/thepit-podcast-template.jpg"},
        {
            'label': plugin.get_string(30008),
            'path': plugin.url_for('episodes8'),
            'thumbnail': "https://www.cbc.ca/radio/podcasts/images/950x950/sactioned-podcast-template.jpg"},
        {
            'label': plugin.get_string(30009),
            'path': plugin.url_for('episodes9'),
            'thumbnail': "https://www.cbc.ca/radio/podcasts/images/promo-secretsofthefifthestate-sm.jpg"},
        {
            'label': plugin.get_string(30010),
            'path': plugin.url_for('episodes10'),
            'thumbnail': "https://www.cbc.ca/radio/podcasts/images/950x950/slumtown-podcast-template.jpg"},
        {
            'label': plugin.get_string(30011),
            'path': plugin.url_for('episodes11'),
            'thumbnail': "https://images.radio-canada.ca/c_scale,w_780,q_auto/v1/cbc-music/programs/1x1/spark.png"},
        {
            'label': plugin.get_string(30012),
            'path': plugin.url_for('episodes12'),
            'thumbnail': "https://www.cbc.ca/radio/podcasts/images/950x950/wiretap2020-podcast-template.jpg"},
        {
            'label': plugin.get_string(30013),
            'path': plugin.url_for('episodes13'),
            'thumbnail': "https://www.cbc.ca/radio/podcasts/images/950x950/world-on-fire-podcast-template.jpg"},
        {
            'label': plugin.get_string(30014),
            'path': plugin.url_for('episodes14'),
            'thumbnail': "https://www.cbc.ca/radio/podcasts/images/promo-bandplayedon.jpg"},
        {
            'label': plugin.get_string(30015),
            'path': plugin.url_for('episodes15'),
            'thumbnail': "https://www.cbc.ca/radio/podcasts/images/promo-cf-sm.jpg"},
        {
            'label': plugin.get_string(30016),
            'path': plugin.url_for('episodes16'),
            'thumbnail': "http://ichef.bbci.co.uk/images/ic/3000x3000/p05bs2wd.jpg"},
        {
            'label': plugin.get_string(30017),
            'path': plugin.url_for('episodes17'),
            'thumbnail': "https://www.cbc.ca/radio/podcasts/images/950x950/atissue-master-podcast-template.jpg"},
        {
            'label': plugin.get_string(30018),
            'path': plugin.url_for('episodes18'),
            'thumbnail': "https://content.production.cdn.art19.com/images/0e/6f/5f/1a/0e6f5f1a-f9b5-44c0-ac02-4da2114f453b/f8a06235821d9afc7bb16a4a0676e6230252b15fd07b57d5e4e96a360073967cfe15d0524b1b2af4441b1f509b3815bb9ce6eb1ec29540bca4e73f0468e00ef1.jpeg"},
        {
            'label': plugin.get_string(30019),
            'path': plugin.url_for('episodes19'),
            'thumbnail': "https://www.cbc.ca/radio/podcasts/images/promo-ambushed.jpg"},

    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items
@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items
@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items
@plugin.route('/episodes4/')
def episodes4():
    soup4 = mainaddon.get_soup4(url4)   
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items
@plugin.route('/episodes5/')
def episodes5():
    soup5 = mainaddon.get_soup5(url5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items
@plugin.route('/episodes6/')
def episodes6():
    soup6 = mainaddon.get_soup6(url6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items
@plugin.route('/episodes7/')
def episodes7():
    soup7 = mainaddon.get_soup7(url7)
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7) 
    items = mainaddon.compile_playable_podcast7(playable_podcast7)
    return items
@plugin.route('/episodes8/')
def episodes8():
    soup8 = mainaddon.get_soup8(url8)
    playable_podcast8 = mainaddon.get_playable_podcast8(soup8)
    items = mainaddon.compile_playable_podcast8(playable_podcast8)
    return items
@plugin.route('/episodes9/')
def episodes9():
    soup9 = mainaddon.get_soup9(url9)
    playable_podcast9 = mainaddon.get_playable_podcast9(soup9)
    items = mainaddon.compile_playable_podcast9(playable_podcast9)
    return items
@plugin.route('/episodes10/')
def episodes10():
    soup10 = mainaddon.get_soup10(url10)
    playable_podcast10 = mainaddon.get_playable_podcast10(soup10)
    items = mainaddon.compile_playable_podcast10(playable_podcast10)
    return items
@plugin.route('/episodes11/')
def episodes11():
    soup11 = mainaddon.get_soup11(url11)
    playable_podcast11 = mainaddon.get_playable_podcast11(soup11)
    items = mainaddon.compile_playable_podcast11(playable_podcast11)
    return items
@plugin.route('/episodes12/')
def episodes12():
    soup12 = mainaddon.get_soup12(url12) 
    playable_podcast12 = mainaddon.get_playable_podcast12(soup12)
    items = mainaddon.compile_playable_podcast12(playable_podcast12)
    return items
@plugin.route('/episodes13/')
def episodes13():
    soup13 = mainaddon.get_soup13(url13)
    playable_podcast13 = mainaddon.get_playable_podcast13(soup13)
    items = mainaddon.compile_playable_podcast13(playable_podcast13)
    return items
@plugin.route('/episodes14/')
def episodes14():
    soup14 = mainaddon.get_soup14(url14)
    playable_podcast14 = mainaddon.get_playable_podcast14(soup14)
    items = mainaddon.compile_playable_podcast14(playable_podcast14)
    return items
@plugin.route('/episodes15/')
def episodes15():
    soup15 = mainaddon.get_soup15(url15)
    playable_podcast15 = mainaddon.get_playable_podcast15(soup15)
    items = mainaddon.compile_playable_podcast15(playable_podcast15)
    return items
@plugin.route('/episodes16/')
def episodes16():
    soup16 = mainaddon.get_soup16(url16)
    playable_podcast16 = mainaddon.get_playable_podcast16(soup16)
    items = mainaddon.compile_playable_podcast16(playable_podcast16)
    return items
@plugin.route('/episodes17/')
def episodes17():
    soup17 = mainaddon.get_soup17(url17)
    playable_podcast17 = mainaddon.get_playable_podcast17(soup17)
    items = mainaddon.compile_playable_podcast17(playable_podcast17)
    return items
@plugin.route('/episodes18/')
def episodes18():
    soup18 = mainaddon.get_soup18(url18)
    playable_podcast18 = mainaddon.get_playable_podcast18(soup18)
    items = mainaddon.compile_playable_podcast18(playable_podcast18)
    return items
@plugin.route('/episodes19/')
def episodes19():
    soup19 = mainaddon.get_soup19(url19)
    playable_podcast19 = mainaddon.get_playable_podcast19(soup19)
    items = mainaddon.compile_playable_podcast19(playable_podcast19)
    return items

if __name__ == '__main__':
    plugin.run()
