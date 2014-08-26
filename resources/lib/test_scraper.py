import unittest
import scraper
import pprint

class EmissionIT(unittest.TestCase):

    def test_get_emissions(self):
        petit_journal = {
            'url': 'http://service.mycanal.fr/page/68645c6a02d5e836da428f9af93d87bb/1277.json',
            'name': 'Le Petit Journal',
            'icon': 'http://media.mycanal.fr/image/50/3/pj212x159.2503.103.png',
        }

        emissions = scraper.Emission.get_emissions()

        # currently there are 41 universities
        self.assertTrue(len(emissions) > 20)

        # hopefully Yale will always be there...
        self.assertTrue(petit_journal in emissions)

class VideoIT(unittest.TestCase):

    def test_from_url(self):
        emission_url = 'http://service.mycanal.fr/page/68645c6a02d5e836da428f9af93d87bb/1277.json'
        test_video = {
            'url': 'http://service.mycanal.fr/getMediaUrl/68645c6a02d5e836da428f9af93d87bb/1107140.json?pfv=hls',
            'name': 'Le Petit Journal du 22/07/14',
            'icon': 'http://media.canal-plus.com/wwwplus/image/4/12/3/nip-nip-21099-640x360-rglrs.10099.jpg',
        }

        videos = scraper.Video.from_url(emission_url)

        # currently there are 41 universities
        self.assertTrue(len(videos) > 20)

        # hopefully Yale will always be there...
        self.assertTrue(test_video in videos)

class MediaIT(unittest.TestCase):

    def test_from_url(self):
        media_url = 'http://service.mycanal.fr/getMediaUrl/68645c6a02d5e836da428f9af93d87bb/1107140.json?pfv=hls'
        test_media = {
            'url': 'http://us-cplus-aka.canal-plus.com/i/1407/22/nip_NIP_21099_,200k,400k,800k,1500k,.mp4.csmil/master.m3u8',
            'name': 'Le Petit Journal du 01/08',
            'icon': 'http://media.canal-plus.com/wwwplus/image/4/12/3/nip-nip-21099-640x360-rglrs.10195.jpg',
        }

        media = scraper.Media.from_url(media_url)

	#pprint.pprint(media)

        # hopefully Yale will always be there...
        self.assertEquals(media, test_media)




if __name__ == '__main__':
    unittest.main()