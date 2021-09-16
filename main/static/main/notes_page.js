$(document).ready(function () {
  $(".treeview-animated").mdbTreeview();
  startTiny();
  $("#full-featured-non-premium").hide();
  tinymce.activeEditor.hide();
});

let useDarkMode = window.matchMedia("(prefers-color-scheme: dark)").matches;

let pagesDisplayId = "#pages";
let treeViewClass = "treeview-animated-element";
let activeTreeViewClass = ".treeview-animated-element.opened";

let contentDiv = ".viewContent";
let textAreaId = "full-featured-non-premium";
let editToggleId = "#viewEditToggle";
let editMode = false;
let saveBtnId = "saveBtn";

$("#" + saveBtnId).click(() => {
  let data = tinymce.get(textAreaId).getContent();
  let csrf_token = $("input[name=csrfmiddlewaretoken]").val();
  let id = $(activeTreeViewClass).attr("id");
  $.post(
    `../../notes/page/update/${id}`,
    {
      content: data,
      csrfmiddlewaretoken: csrf_token,
    },
    (data, success) => {
      console.log(success);
    }
  );
});

$(editToggleId).change(function () {
  editMode = !$(this).prop("checked");
  if (editMode) {
    changeToEditMode();
  } else {
    changeToViewMode();
  }
});

function changeToEditMode(data = null) {
  let content = data === null ? $(contentDiv).html() : data;
  tinymce.activeEditor.show();
  //$("#" + textAreaId).show();
  if (content === "" || content === null) {
    content = ""
  }
  tinymce.get(textAreaId).setContent(content);
  $(contentDiv).hide();
}

function changeToViewMode(data = null) {
  let content = data === null ? tinymce.activeEditor.getContent() : data;
  if (content === "" || content === null) {
    content = ""
  }
  $(contentDiv).html(content);
  $(contentDiv).show();
  tinymce.activeEditor.hide();
  $("#" + textAreaId).hide();
}

function showNote(id) {
  let elem = id;
  $.get(`../../notes/page/${elem}`, (data, status) => {
    if (status === "success") {
      let content = data["content"];
      if (editMode) {
        changeToEditMode(content);
        //$(textAreaClass).attr("value", content);
      } else {
        changeToViewMode(content);
      }
    }
  });
}

$("#add_btn_form").click(() => {
  let id;
  let title = $("#nameForm").val();
  $("#nameForm").val("");
  if (title === "") {
  } else {
    let csrf_token = $("input[name=csrfmiddlewaretoken]").val();
    let note_id = $("input[name=noteId").val();
    $.post(
      "../../notes/page/create/",
      {
        title: title,
        note_id: note_id,
        csrfmiddlewaretoken: csrf_token,
      },
      (data, status) => {
        if (status === "success") {
          let elem = `<li
                      class="${treeViewClass}"
                      id="${parseInt(data.trim())}"
                      onclick="showNote(this.id)"
                      >
                      <p>${title}</p>
                      </li>`;
          $(pagesDisplayId).append(elem);
          $(".treeview-animated").mdbTreeview();
          $("#modalPageName").modal("hide");
        } else {
          alert("An error occured");
          $("#modalPageName").modal("hide");
        }
      }
    );
  }
});

function startTiny() {
  tinymce.init({
    selector: "textarea#full-featured-non-premium",
    plugins:
      "print preview paste importcss searchreplace autolink autosave save directionality code visualblocks visualchars fullscreen image link media template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists wordcount imagetools textpattern noneditable help charmap quickbars emoticons",
    imagetools_cors_hosts: ["picsum.photos"],
    toolbar:
      "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist | forecolor backcolor removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media template link anchor codesample | ltr rtl",
    toolbar_sticky: true,
    autosave_ask_before_unload: true,
    autosave_interval: "30s",
    autosave_prefix: "{path}{query}-{id}-",
    autosave_restore_when_empty: false,
    autosave_retention: "2m",
    image_advtab: true,
    link_list: [
      { title: "My page 1", value: "https://www.tiny.cloud" },
      { title: "My page 2", value: "http://www.moxiecode.com" },
    ],
    image_list: [
      { title: "My page 1", value: "https://www.tiny.cloud" },
      { title: "My page 2", value: "http://www.moxiecode.com" },
    ],
    image_class_list: [
      { title: "None", value: "" },
      { title: "Some class", value: "class-name" },
    ],
    importcss_append: true,
    file_picker_callback: function (callback, value, meta) {
      /* Provide file and text for the link dialog */
      if (meta.filetype === "file") {
        callback("https://www.google.com/logos/google.jpg", {
          text: "My text",
        });
      }

      /* Provide image and alt text for the image dialog */
      if (meta.filetype === "image") {
        callback("https://www.google.com/logos/google.jpg", {
          alt: "My alt text",
        });
      }

      /* Provide alternative source and posted for the media dialog */
      if (meta.filetype === "media") {
        callback("movie.mp4", {
          source2: "alt.ogg",
          poster: "https://www.google.com/logos/google.jpg",
        });
      }
    },
    templates: [
      {
        title: "New Table",
        description: "creates a new table",
        content:
          '<div class="mceTmpl"><table width="98%%"  border="0" cellspacing="0" cellpadding="0"><tr><th scope="col"> </th><th scope="col"> </th></tr><tr><td> </td><td> </td></tr></table></div>',
      },
      {
        title: "Starting my story",
        description: "A cure for writers block",
        content: "Once upon a time...",
      },
      {
        title: "New list with dates",
        description: "New List with dates",
        content:
          '<div class="mceTmpl"><span class="cdate">cdate</span><br /><span class="mdate">mdate</span><h2>My List</h2><ul><li></li><li></li></ul></div>',
      },
    ],
    template_cdate_format: "[Date Created (CDATE): %m/%d/%Y : %H:%M:%S]",
    template_mdate_format: "[Date Modified (MDATE): %m/%d/%Y : %H:%M:%S]",
    height: 600,
    image_caption: true,
    quickbars_selection_toolbar:
      "bold italic | quicklink h2 h3 blockquote quickimage quicktable",
    noneditable_noneditable_class: "mceNonEditable",
    toolbar_mode: "sliding",
    contextmenu: "link image imagetools table",
    skin: useDarkMode ? "oxide-dark" : "oxide",
    content_css: useDarkMode ? "dark" : "default",
    content_style:
      "body { font-family:Helvetica,Arial,sans-serif; font-size:14px }",
  });
}
