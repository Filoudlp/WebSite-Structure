from ._anvil_designer import deflection_POUTemplate
from anvil import *
from routing import router
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from plotly import graph_objs as go

from ..... import norme


class deflection_POU(deflection_POUTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.layout.fun_show_sidesheet(False)

    # Any code you write here will run before the form opens.

  @handle("btn_calc", "click")
  def btn_calc_click(self, **event_args):
    """This method is called when the component is clicked."""
    API_URL = "/api/deflection_calc"
    payload = {
      "length": float(self.geo_def_1.txb_length.text),
      "E": float(self.sec_type_1.tbx_E.text),
      "b": float(self.geo_def_1.txb_b.text),
      "h": float(self.geo_def_1.txb_h.text),
      "A": float(self.geo_def_1.txb_A.text),
      "Iy": float(self.geo_def_1.txb_Iy.text),
      "Iz": float(self.geo_def_1.txb_Iz.text),
      "load": float(self.effort_def_1.txb_load.text),
    }
    response = norme.api_call(API_URL, payload)
    print(response)

    print(response["b"]["x"])
    x = response["b"]["x"]
    m = response["b"]["M"]
    v = response["b"]["V"]
    n = response["b"]["N"]


    trace0 = go.Scatter(
      x = x,
      y = m,
      name = 'Bending moment',
      line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 1)
    )
    trace1 = go.Scatter(
      x = x,
      y = v,
      name = 'Shear force',
      line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 1)
    )
    trace2 = go.Scatter(
      x = x,
      y = n,
      name = 'normal force',
      line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 1)
    )
    self.plot_cm_1.plot_1.data = [trace0, trace1, trace2]

    self.plot_cm_1.plot_1.layout = dict(title = 'Effort interne',
                 xaxis = dict(title = 'Angle'),
                  yaxis = dict(title = 'Effort interne'),
    )

    