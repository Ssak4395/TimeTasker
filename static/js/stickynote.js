var num_notes = 0;
var maxh = $('#ctn-notes').height();
var maxw = $('#ctn-notes').width();
var ctn = document.getElementsByClassName('#ctn-notes');
var arr_notes = [];
$(document).ready(function () {
    var _class1 = '';
    var _class2 = '';
    var note_id = '';
    var del_btn_no = '';
    $('.add-note').click(function () {
        // container of head bar and note
        _class1 = 'note-wrapper' + num_notes;
        var _div = $('<div></div>');
        _div.attr({
            'class': _class1,
            'style': 'position: absolute; top: 25%; right: 4%; width: 25%; height: 40%; max-height: ' + maxh + '; max-width: ' + maxw + '; background: black; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);'
        });
        // head bar for note management
        _class2 = 'note-head-bar' + num_notes;
        var note_head_bar = $('<div></div>');
        note_head_bar.attr({
            'class': _class2,
            'style': 'position: absolute; top: 0; width: 100%; height: 20%; background: white;'
        });
        // new note
        note_id = 'note' + num_notes;
        var _textarea = $('<textarea></textarea>');
        _textarea.attr({
            'id': note_id,
            'style': 'position: absolute; bottom: 0; width: 100%; height: 80%; background: blue; background: linear-gradient(to bottom right, #ffffff 0%, #00ccff 100%); resize: none; border: none;'
        });
        // delete button placed on head bar
        del_btn_no = 'del-btn' + num_notes;
        var del_btn = $('<i></i>');
        del_btn.attr({
            'class': 'fa fa-times ' + del_btn_no,
            'style': 'position: absolute; top: 5px; left: 5px;',
            'data-toggle': 'modal',
            'data-target': '#del-confirm'
        });
        // save button placed on head bar
        save_btn_no = 'save-btn' + num_notes;
        var save_btn = $('<i></i>');
        save_btn.attr({
            'class': 'fa fa-save ' + save_btn_no,
            'style': 'position: absolute; top: 5px; right: 5px;',
            'data-toggle': 'modal',
            'data-target': '#save-confirm'
        });
        arr_notes.push(del_btn_no);
        _div.appendTo('#ctn-notes');
        note_head_bar.appendTo('.' + _class1)
        _textarea.appendTo('.' + _class1);
        del_btn.appendTo('.' + _class2);
        save_btn.appendTo('.' + _class2);
        _div.draggable({
            containment: 'parent'
        });
        _div.resizable({
            animate: true,
            maxHeight: $('#ctn-notes').height(),
            maxWidth: $('#ctn-notes').width(),
            minHeight: '100',
            minWidth: '100'
        });
        $('div' + '.ui-resizable-handle').attr({
            'style': 'z-index: 0'
        });
        $('.' + del_btn_no).click(function () {
            // alert($(this)[0].classList[2]);
            // $($(this).parent().parent().parent()[0]).attr('id');
            var _remove_this = $(this).parent().parent()[0].classList[0];
            $('.btn-primary').click(function () {
                $('.' + _remove_this).remove();
            });
        });
        $('.' + save_btn_no).click(function () {
            $('.btn-primary').click(function () {
                // TODO
            });
        });
        num_notes++;
    });
});


$("i").trigger("click");