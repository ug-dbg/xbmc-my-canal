# -*- coding: utf-8 -*-
import unittest
import scraper
import pprint

class EmissionIT(unittest.TestCase):

    def test_get_emission_types(self):
        emissions_category = {
            'name': 'Emissions',
            'index': 0,
        }
        emission_types = scraper.Emission.get_emission_types()

        # currently there are 7 categories or 'emission types'
        self.assertGreater(len(emission_types), 3)
        self.assertTrue(emissions_category in emission_types)

    def test_get_emissions_from_index(self):
        emissions = scraper.Emission.get_emissions_from_index(0)

        # Hope there are at least 5 available different shows
        self.assertGreater(len(emissions), 5)

        # hopefully 'Le petit journal' will always be there...
        for emission in emissions:
		if(emission["name"] == 'Le Petit Journal'):
			return
        self.assertFail("Le petit journal is not available!")

class VideoIT(unittest.TestCase):

    def test_from_url(self):
        emission = scraper.Emission.get_emissions_from_index(0)[0]
        videos   = scraper.Video.from_url(emission["url"])

        # currently there are 24 videos
        self.assertGreater(len(videos), 10)

class MediaIT(unittest.TestCase):

    def test_from_url(self):
        #The media URL for a video of an emission should have an m3u8 suffix
        emission = scraper.Emission.get_emissions_from_index(0)[2]
        videos   = scraper.Video.from_url(emission["url"])
        media    = scraper.Media.from_url(videos[0]["url"])
        self.assertEquals(".m3u8", media["url"][-5:])

if __name__ == '__main__':
    unittest.main()
