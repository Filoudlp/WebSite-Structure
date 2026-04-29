from ._anvil_designer import RowItemTemplate
from anvil import *


class RowItem(RowItemTemplate):
  def __init__(self, name="", value="", unit="", formula="",
               ref="", editable=False, row_type="input", **properties):
    self.init_components(**properties)

    self.lbl_name.text = name
    self.lbl_unit.text = unit
    self.lbl_formula.text = formula
    self.lbl_ref.text = ref

    if editable:
      self.tb_value.text = str(value)
      self.tb_value.visible = True
      self.lbl_value.visible = False
      self.tb_value.background = "#FCE4D6"  # orange Excel
    else:
      self.lbl_value.text = str(value)
      self.tb_value.visible = False
      self.lbl_value.visible = True

      # Couleur de fond selon type
    colors = {
      "input": "#FFFFFF",
      "param": "#DDEBF7",
      "result": "#FFFFFF",
      "ok": "#C6EFCE",
      "nok": "#FFC7CE",
    }
    self.background = colors.get(row_type, "#FFFFFF")

    # Event sur changement
    self.tb_value.set_event_handler('change', self._on_change)

  def _on_change(self, **event_args):
    self.raise_event('x-value-changed')

  @property
  def value(self):
    if self.tb_value.visible:
      try:
        return float(self.tb_value.text)
      except (ValueError, TypeError):
        return 0.0
    return self.lbl_value.text
