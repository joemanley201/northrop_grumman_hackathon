$(document).ready(function() {
    var table = $("#analysisTable")

    html = ""
    for (var i = 0, course_length = response.course_list.length; i < course_length; i++) {
        html += '<h2>' + response.course_list[i] + '</h2>';
        for (var j = 0, metric_length = response.metric_list.length; j < metric_length; j++) {
            html += '<div class="row"><div class="col-md-4">' + response.metric_list[(i * 11) + j] + '</div><div class="col-md-4"><span class="glyphicon glyphicon-chevron-up success" aria-hidden="true"></span>' + response.increase_list[(i * 11) + j] + '</div></div>'
        }
    }
    html += '<div class="row"><div class="col-md-4">Hi</div><div class="col-md-4">Hello</div></div>'
    table.append(html)
});