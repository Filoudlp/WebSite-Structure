from ._anvil_designer import compressionTemplate
from anvil import *
import anvil.server
from routing import router
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class compression(compressionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.geometrie_pou_1.txb_length.visible = False
    self.geometrie_pou_1.lbl_length.visible = False

    self.geometrie_pou_1.txb_b.visible = False
    self.geometrie_pou_1.lbl_b.visible = False

    self.geometrie_pou_1.txb_h.visible = False
    self.geometrie_pou_1.lbl_h.visible = False

    self.geometrie_pou_1.txb_e.visible = False
    self.geometrie_pou_1.lbl_e.visible = False

    self.geometrie_pou_1.txb_Av.visible = False
    self.geometrie_pou_1.lbl_av.visible = False

    self.geometrie_pou_1.txb_Iy.visible = False
    self.geometrie_pou_1.lbl_Iy.visible = False

    self.geometrie_pou_1.txb_Iz.visible = False
    self.geometrie_pou_1.lbl_Iz.visible = False

    self.geometrie_pou_1.txb_Wy.visible = False
    self.geometrie_pou_1.lbl_Wy.visible = False

    self.geometrie_pou_1.txb_Wz.visible = False
    self.geometrie_pou_1.lbl_Wz.visible = False

    # Any code you write here will run before the form opens.
