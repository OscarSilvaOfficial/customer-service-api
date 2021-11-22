import pytest
from api import application


class BaseTests:

  @pytest.fixture(scope='module')
  def app(self):
    app = application()
    return app