from distutils.debug import DEBUG

from instance.config import MOVIE_API_KEY


class Config:
  '''
  General configuration parent class
  '''
  MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'


class ProdConfig(Config):
  '''
  Production configuration child class

  Args:
    Config: The Parent configuration class with general config settings
  '''
  pass


class DevConfig(Config):
  '''
  Development configuration child class
  
  Args:
    Config: The Parent configuration class with general config settings
  '''
  DEBUG = True