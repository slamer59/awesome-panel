"""
# Wired Elements

<wired-link href="https://wiredjs.com/">Wired JS</wired-link> is a set of common UI elements with a hand-drawn, sketchy look. These can be used for
wireframes, mockups, or just the fun hand-drawn look.

You can find inspiration at the <wired-link href="https://wiredjs.com/showcase.html">Wired JS Showcase</wired-link>

You might combine the Wired elements with

- **Sketchy Plots** generated by <wired-link href="https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.xkcd.html">matplotlib.pyplot.xkcd</wired-link> or
- **Sketchy Drawings** via <wired-link ref="https://roughjs.com/">rough.js</wired-link>.

<img style="height:480px;width:640px" alt="https://matplotlib.org/3.1.1/_images/sphx_glr_xkcd_001.png" src="https://matplotlib.org/3.1.1/_images/sphx_glr_xkcd_001.png">

If you want a Wired notebook example added to the Panel Gallery then please upvote
<wired-link href="https://github.com/holoviz/panel/pull/1263">Panel PR 1263</wired-link>.

Please note that this is **work in progress**. If you experience bugs and would like improvements
please file them at <wired-link href="https://github.com/marcskovmadsen/awesome-panel">github/marcskovmadsen/awesome-panel</wired-link>.

**Author:**
<wired-link href="https://datamodelanalytics.com">Marc Skov Madsen</wired-link>
(<wired-link href="https://awesome-panel.org">awesome-panel.org</wired-link>)

**Code**
[This Page](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/application/pages/awesome_panel_express_tests/test_wired.py)
[Wired Elements](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/package/awesome_panel/express/components/wired.py)

**Resources:**
<wired-link href="https://github.com/wiredjs/wired-elements">Wired GitHub</wired-link>

**Tags:**
<wired-link href="https://wiredjs.com/">Wired</wired-link>,
<wired-link href="https://panel.holoviz.org/">Panel</wired-link>,
<wired-link href="https://www.python.org/">Python</wired-link>
"""
import datetime as dt

import pandas as pd
import panel as pn
import param

from awesome_panel.express.components import wired


def test_wired_view():
    show_html = False

    def section(component, message=None, show_html=show_html):
        title = "## " + str(type(component)).split(".")[4][:-2]

        parameterset = set(component._child_parameters())
        if show_html:
            parameterset.add("html")
        for parameter in component.parameters_to_watch:
            parameterset.add(parameter)

        parameters = list(parameterset)
        if message:
            return (
                title,
                component,
                pn.Param(component, parameters=parameters),
                pn.pane.Markdown(message),
                pn.layout.Divider(),
            )
        return (
            pn.pane.Markdown(title),
            component,
            pn.Param(component, parameters=parameters),
            pn.layout.Divider(),
        )

    button = wired.Button()
    check_box = wired.Checkbox()
    check_box_checked = wired.Checkbox(value=True)
    date_picker = wired.DatePicker()
    dialog = wired.Dialog(text="Lorum Ipsum. Panel is awesome!")
    divider = wired.Divider()
    fab = wired.Fab()
    float_slider = wired.FloatSlider()
    icon_button = wired.IconButton()
    int_slider = wired.IntSlider()
    image = wired.Image(
        object="https://www.gstatic.com/webp/gallery/1.sm.jpg", height=200, width=300
    )
    link = wired.Link(href="https://panel.holoviz.org/", text="HoloViz", target="_blank")
    # literal_input = wired.LiteralInput(default={"a": 1, "b": "hello app world"})
    progress = wired.Progress(value=50)
    progress_spinner = wired.ProgressSpinner()
    radio_button = wired.RadioButton()
    search_input = wired.SearchInput()
    select = wired.Select(
        html="""<wired-combo id="colorCombo" selected="red" role="combobox" aria-haspopup="listbox" tabindex="0" class="wired-rendered" aria-expanded="false"><wired-item value="red" aria-selected="true" role="option" class="wired-rendered">Red</wired-item><wired-item value="green" role="option" class="wired-rendered">Green</wired-item><wired-item value="blue" role="option" class="wired-rendered">Blue</wired-item></wired-combo>"""
    )
    text_area = wired.TextAreaInput()
    text_input = wired.TextInput()
    toggle = wired.Toggle()
    video = wired.Video(
        autoplay=True,
        loop=True,
        object="https://file-examples.com/wp-content/uploads/2017/04/file_example_MP4_480_1_5MG.mp4",
    )
    section(select)
    return pn.Column(
        *section(button),
        *section(check_box),
        *section(check_box_checked),
        *section(date_picker),
        *section(dialog),
        *section(divider),
        *section(fab),
        *section(float_slider,),
        *section(icon_button),
        *section(image),
        *section(int_slider,),
        *section(
            link,
            "Normally you would just use the `<wired-link>` tag directly in your html or markdown text",
        ),
        # Todo: Fix AssertionError
        # *section(literal_input),
        *section(progress),
        *section(radio_button),
        *section(search_input),
        *section(select),
        *section(progress_spinner),
        *section(text_area),
        *section(text_input),
        *section(toggle),
        *section(video),
        name="Elements",
    )


def test_param_view():
    class BaseClass(param.Parameterized):
        x = param.Parameter(default=3.14, doc="X position")
        y = param.Parameter(default="Not editable", constant=True)
        string_value = param.String(default="str", doc="A string")
        num_int = param.Integer(50000, bounds=(-200, 100000))
        unbounded_int = param.Integer(23)
        float_with_hard_bounds = param.Number(8.2, bounds=(7.5, 10))
        float_with_soft_bounds = param.Number(0.5, bounds=(0, None), softbounds=(0, 2))
        unbounded_float = param.Number(30.01, precedence=0)
        hidden_parameter = param.Number(2.718, precedence=-1)
        integer_range = param.Range(default=(3, 7), bounds=(0, 10))
        float_range = param.Range(default=(0, 1.57), bounds=(0, 3.145))
        dictionary = param.Dict(default={"a": 2, "b": 9})

    class Example(BaseClass):
        """An example Parameterized class"""

        timestamps = []

        boolean = param.Boolean(True, doc="A sample Boolean parameter")
        color = param.Color(default="#FFFFFF")
        date = param.Date(
            dt.datetime(2017, 1, 1), bounds=(dt.datetime(2017, 1, 1), dt.datetime(2017, 2, 1))
        )
        dataframe = param.DataFrame(pd.util.testing.makeDataFrame().iloc[:3])
        select_string = param.ObjectSelector(default="yellow", objects=["red", "yellow", "green"])
        select_fn = param.ObjectSelector(default=list, objects=[list, set, dict])
        int_list = param.ListSelector(default=[3, 5], objects=[1, 3, 5, 7, 9], precedence=0.5)
        single_file = param.FileSelector(path="../../*/*.py*", precedence=0.5)
        multiple_files = param.MultiFileSelector(path="../../*/*.py?", precedence=0.5)
        record_timestamp = param.Action(
            lambda x: x.timestamps.append(dt.datetime.utcnow()),
            doc="""Record timestamp.""",
            precedence=0.7,
        )

    base = Example()
    parameters = [
        "x",
        "y",
        "string_value",
        "num_int",
        "unbounded_int",  # Todo: Add Feature Request for unbounded int to Wired
        "float_with_hard_bounds",
        "float_with_soft_bounds",
        "unbounded_float",  # Todo: Add Feature Request for unbounded int to
        "hidden_parameter",
        # "integer_range",  # Todo: Add Feature Request for Integer Range to Wired
        # "float_range",  # Todo: Add Feature Request for Float Range to Wired
        "dictionary",
        "boolean",
        # "color", # Todo: Add Feature Request for Color Picker to Wired
        "date",
        # "dataframe", # Todo: Add Feature Request for Table to Wired
        "select_string",
    ]
    widgets = {
        # Todo: Implement spinner to support Numbers
        # "x": wired.TextInput,  # Todo: Find out why value is not shown on construction
        "y": wired.TextInput,  # Todo: Find out why value is not shown on construction
        "string_value": wired.TextInput,  # Todo: Find out why value is not shown on construction
        "num_int": wired.IntSlider,  # Todo: Add value to label
        "unbounded_int": wired.TextInput,  # Todo: Find out why unbounded_int does not use TextInput
        "float_with_hard_bounds": wired.FloatSlider,  # Todo: Add value to label
        "float_with_soft_bounds": wired.FloatSlider,  # Todo: Add value to label
        "unbounded_float": wired.TextInput,  # Todo: Find out why unbounded_int does not use TextInput
        "dictionary": wired.LiteralInput,
        "boolean": wired.Checkbox,
        "date": wired.DatePicker,
        "select_string": wired.Select,
    }
    pn.Param(base, parameters=parameters, widgets=widgets)
    # @Philippfr: how do I get wired widgets to stretch_width automatically?
    return pn.Column(
        pn.Row(
            pn.Param(base, parameters=parameters),
            pn.Param(base, parameters=parameters, widgets=widgets),
        ),
        name="Param",
    )


def view():
    css_and_js = """
<script src="https://unpkg.com/@webcomponents/webcomponentsjs@2.2.7/webcomponents-loader.js"></script>
<script src="https://wiredjs.com/dist/showcase.min.js"></script>
<link href="https://wiredjs.com/fonts/font.woff2" as="font">
<style>
    @font-face {
      font-family: 'Gloria Hallelujah';
      font-style: normal;
      font-weight: 400;
      font-display: fallback;
      src: local('Gloria Hallelujah'), local('GloriaHallelujah'), url(https://wiredjs.com/fonts/font.woff2) format('woff2');
      unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
    }
</style>
<style>
.bk-root .bk .wired-intro * {
    font-size: 16px;
    font-family: 'Gloria Hallelujah', sans-serif;
}
.bk-root .bk .wired-intro h1 {
    font-size: 32px;
    font-weight: 900;
}
.bk-root .bk.wired-bar h1 {
    color: rgb(240, 230, 244);
    font-family: 'Gloria Hallelujah', sans-serif;
    font-size: 36px;
    margin:0px;
    margin-block:0px;
}
</style>
"""

    css_and_js_pane = pn.pane.HTML(css_and_js, height=0, width=0, margin=0, sizing_mode="fixed")

    intro = pn.pane.Markdown(__doc__, css_classes=["wired-intro"])
    bar = pn.Row(
        pn.pane.PNG(wired.LOGO, width=50, height=50, sizing_mode="fixed"),
        pn.pane.Markdown("# Wired Elements"),
        sizing_mode="stretch_width",
        height=60,
        background=wired.GRAY,
        margin=(25, 0, 25, 0),
        css_classes=["wired-bar"],
    )

    wired_view = test_wired_view()
    param_view = test_param_view()
    tabs = pn.layout.Tabs(wired_view, param_view)
    return pn.Column(css_and_js_pane, intro, bar, tabs)


if __name__.startswith("bokeh"):
    pn.config.sizing_mode = "stretch_width"
    view().servable()
