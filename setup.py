from setuptools import setup
setup(
      name = 'ahsay',
      packages = ['ahsay'], # this must be the same as the name above
      version = '0.1.3',
      description = 'A simple requests wrapper for the Ahsay API',
      author = 'Kristjan Oddsson',
      author_email = 'koddsson@gmail.com',
      url = 'https://github.com/koddsson/ahsay-python-api', # use the URL to the github repo
      download_url = 'https://github.com/koddsson/ahsay-python-api/tarball/0.1.3', # I'll explain this in a second
      keywords = ['ahsay', 'backup', 'api'], # arbitrary keywords
      classifiers = [],
      install_requires = [
        'docopt==0.6.2',
        'requests==2.4.1'
      ],
)
