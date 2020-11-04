import argparse
import sys
import webbrowser

socialmedias = [
    {
        'name': 'facebook',
        'url': 'https://www.facebook.com',
        'keywords': ['facebook', 'fb']
    },
    {
        'name': 'twitter',
        'url': 'https://www.twitter.com',
        'keywords': ['twitter', 'tw']
    },
    {
        'name': 'instagram',
        'url': 'https://www.instagram.com',
        'keywords': ['instagram', 'insta', 'in']
    },
    {
        'name': 'spotify',
        'url': 'https://open.spotify.com/',
        'keywords': ['spotify', 'sp', 'spoty']
    },
    {
        'name': 'linkedin',
        'url': 'https://www.linkedin.com',
        'keywords': ['linkedin', 'link', 'li']
    },
    {
        'name': 'youtube',
        'url': 'https://www.youtube.com',
        'keywords': ['youtube', 'yt']
    },
    {
        'name': 'codechef',
        'url': 'https://www.codechef.com',
        'keywords': ['codechef', 'cd']
    },
    {
        'name': 'codeforces',
        'url': 'https://www.codeforces.com',
        'keywords': ['codeforces', 'cf']
    },
    {
        'name': 'hackerrank',
        'url': 'https://www.hackerrank.com',
        'keywords': ['hackerrank', 'hr']
    },
    {
        'name': 'hackerearth',
        'url': 'https://www.hackerearth.com',
        'keywords': ['hackerearth', 'he']
    },
    {
        'name': 'github',
        'url': 'https://www.github.com/sumit-kushwah',
        'keywords': ['github', 'gh']
    },
    {
        'name': 'leetcode',
        'url': 'https://www.leetcode.com',
        'keywords': ['leetcode', 'lt']
    },
    {
        'name': 'kaggle',
        'url': 'https://www.kaggle.com',
        'keywords': ['kaggle', 'kg']
    },
]


parser = argparse.ArgumentParser(description='Open social media sites in your default broweser.')
parser.add_argument('inputmedias', help='name of social media', nargs='+')

if len(sys.argv) <= 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
inputmedias = args.inputmedias

for socialmedia in socialmedias:
    if len(set(socialmedia['keywords']).intersection(set(inputmedias))) > 0:
        webbrowser.open(socialmedia['url'])
    