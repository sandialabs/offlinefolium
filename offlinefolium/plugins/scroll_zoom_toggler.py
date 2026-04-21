from branca.element import MacroElement

from offlinefolium.template import Template


class ScrollZoomToggler(MacroElement):
    """Creates a button for enabling/disabling scroll on the Map."""

    _template = Template(
        """
        {% macro header(this,kwargs) %}
            <style>
                #{{ this.get_name() }} {
                    position:absolute;
                    width:35px;
                    bottom:10px;
                    height:35px;
                    left:10px;
                    background-color:#fff;
                    text-align:center;
                    line-height:35px;
                    vertical-align: middle;
                    }
            </style>
        {% endmacro %}

        {% macro html(this,kwargs) %}
            <img id="{{ this.get_name() }}"
                 alt="scroll"
                 src="data:image/png;base64,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"
                 style="z-index: 999999"
                 onclick="{{ this._parent.get_name() }}.toggleScroll()">
            </img>
        {% endmacro %}

        {% macro script(this,kwargs) %}
            {{ this._parent.get_name() }}.scrollEnabled = true;

            {{ this._parent.get_name() }}.toggleScroll = function() {
                if (this.scrollEnabled) {
                    this.scrollEnabled = false;
                    this.scrollWheelZoom.disable();
                } else {
                    this.scrollEnabled = true;
                    this.scrollWheelZoom.enable();
                }
            };
            {{ this._parent.get_name() }}.toggleScroll();
        {% endmacro %}
        """
    )

    def __init__(self):
        super().__init__()
        self._name = "ScrollZoomToggler"
