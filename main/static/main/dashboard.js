/*$("#add_btn_form").click(() => {
  let id;
  let title = $("#nameForm").val();
  $("#nameForm").val("");
  if (title === "") {
  } else {
    let csrf_token = $("input[name=csrfmiddlewaretoken]").val();
    $.post(
      "../../notes/create/",
      {
        title: title,
        csrfmiddlewaretoken: csrf_token,
      },
      (data, status) => {
        console.log("Success")
      }
    );
  }
});*/
let notes_container = "notes_container"

function sortAccordingToRelevance() {
  $("#" + notes_container).html(relevanceSortHtml)
}

function sortAccordingToTitle() {
  $("#" + notes_container).html(titleSortHtml)
}