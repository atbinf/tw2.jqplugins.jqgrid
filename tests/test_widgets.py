from tw2.core.testbase import (
    WidgetTest as _WidgetTest,
)

import tw2.jqplugins.jqgrid.widgets as w


class WidgetTest(_WidgetTest):
    engines = ['mako', 'genshi']


class TestJQGridWidget(WidgetTest):
    widget = w.jqGridWidget
    attrs = {'id' : 'foo'}
    params = {'options' : {
        'data': [
            { 'field1' : 'foo', 'field2' : 'foo' } for i in range(2)
        ],
        'datatype': "local",
        'colNames':['Field1', 'Field2'],
        'colModel':[
            {'name':'field1'},
            {'name':'field2'},
            ],
        'viewrecords': True,
        'rowNum':100,
        'rowList':[100,200],
        'caption':"Example"
    }}
    expected = """
<div>
<table id="foo"></table>
<script type="text/javascript">
$(document).ready(
    function(){
        var opts = {"viewrecords": true, "rowList": [100, 200], "colModel": [{"name": "field1"}, {"name": "field2"}], "caption": "Example", "datatype": "local", "colNames": ["Field1", "Field2"], "data": [{"field2": "foo", "field1": "foo"}, {"field2": "foo", "field1": "foo"}], "rowNum": 100};
        var grid = $("#foo");
        grid.jqGrid(opts);
        if ( 'pager' in opts ) {
            opts['pager_selector'] = opts['pager'];
            opts['pager'] = $(opts['pager'])
            var pager_opts = {}
            var prmEdit = {};
            var prmAdd = {};
            var prmDel = {};
            var prmSearch = {};
            var prmView  = {};
            grid.navGrid('#'+opts['pager_selector'], pager_opts,
                         prmEdit, prmAdd, prmDel, prmSearch, prmView)
            ;
        }
    }
);
</script>
</div>"""
