
var flag = true;
$(document).ready(function () {
  $("#tab1").on("keyup", function (event) {
    if (event.keyCode === 13) {
      $("#log").click();
    }
  });
  $("#tab2").on("keyup", function (event) {
    if (event.keyCode === 13) {
      $("#sign").click();
    }
  });
  $("#tab3").on("keyup", function (event) {
    if (event.keyCode === 13) {
      $("#forgot").click();
    }
  });
  $("#auto").click(function () {
    if ($(".d7 .b1").text().trim() == "Sign Up") {
      $(".d3").css({
        translate: "101% 0",
        transition: "0.5s",
        "border-top-right-radius": "5px",
        "border-bottom-right-radius": "5px",
        "border-top-left-radius": "0px",
        "border-bottom-left-radius": "0px",
      });
      $(".d7").css({ translate: "-100% 0", transition: "0.5s" });
      $(".d7 .b1").text("Sign In");
      $(".d7 p").text("Existing User");
      $(".d3 .b1").text("Sign Up");
      $(".d3 h1").text("Sign Up");
      $(".d3 h1").css({ "font-size": "3rem" });
      $("#tab2").attr("hidden", false);
      $("#tab1").attr("hidden", true);
      $("#tab3").attr("hidden", true);
    } else {
      $(".d3").css({
        translate: "0 0",
        transition: "0.5s",
        "border-top-right-radius": "0px",
        "border-bottom-right-radius": "0px",
        "border-top-left-radius": "5px",
        "border-bottom-left-radius": "5px",
      });
      $(".d7").css({ translate: "0 0", transition: "0.5s" });
      $(".d7 .b1").text("Sign Up");
      $(".d7 p").text("New User");
      $(".d3 .b1").text("Log In");
      $(".d3 h1").text("Log In");
      $(".d3 h1").css({ "font-size": "4rem" });
      $("#tab2").attr("hidden", true);
      $("#tab3").attr("hidden", true);
      $("#tab1").attr("hidden", false);
    }
  });
  $("span").click(function () {
    $("#tab3").attr("hidden", false);
    $("#tab1").attr("hidden", true);
    $(".d3 h1").text("Forgot Password");
    $(".d3 h1").css({ "font-size": "2rem" });
    $(".d3 .b1").text("Create");
  });
  $("#stu").click(function () {
    $("#student,#student1").attr("hidden", false);
    $("#employee").attr("hidden", true);
  });
  $("#emp").click(function () {
    $("#student,#student1").attr("hidden", true);
    $("#employee").attr("hidden", false);
  });
  function fl(iid) {
    if ($(iid).val().trim() == "") flag = false;
  }
  $("#sign").click(function () {
    flag = true;
    if (
      $("#stu").prop("checked") == false &&
      $("#emp").prop("checked") == false
    ) {
      flag = false;
      swal("Warning", "Please Select any Student/Employee!!",'warning');
    } else if (
      $("#tab2 #pas").val().trim() != $("#tab2 #cpas").val().trim()
    ) {
      swal("Error", "Please enter same password in confirm password!!", "error");
      flag = false;
    } else {
      fl("#tab2 #name");
      fl("#tab2 #email");
      fl("#tab2 #ans");
      fl("#tab2 #pas");
      fl("#tab2 #cpas");
      if (flag == false) {
        swal("Warning", "Please fill all field!!", "warning");
      }
    }
    if (flag) {
      if (confirm("Do You want to create your account!!")) {
        $.ajax({
          method: "post",
          url: "pythonfile/login.py",
          data: {
            cond: "entry",
            t1: $("#tab2 #name").val().trim(),
            t2: $("#tab2 #email").val().trim(),
            t3: $("#tab2 #secq").val().trim(),
            t4: $("#tab2 #ans").val().trim(),
            t5: $("#tab2 #pas").val().trim(),
            t6:$('input[name="a"]:checked').val(),
          },
          success: function (data) {
            data = data.split("&&");
            swal('Message',data[0],'info').then((value) => {
              location.reload()
            });
            // if (data[1] == 0)location.reload();
          },
        });
      }
    }
  });
  $("#log").click(function () {
    flag = true;
    fl("#tab1 #email");
    fl("#tab1 #pas");
    if (flag) {
      $.ajax({
        method: "post",
        url: "pythonfile/login.py",
        data: {
          cond: "login",
          t1: $("#tab1 #email").val().trim(),
          t2: $("#tab1 #pas").val().trim(),
        },
        success: function (data) {
          if(data!=0){
              data=data.split('&&');
              window.location='Dashboard.html';
              sessionStorage.setItem('uname',data[0].trim());
              sessionStorage.setItem('email',data[1].trim());
              sessionStorage.setItem('user_type',data[2].trim());
          } else {
            swal('Error',"Invalid Username or Password!!",'error');
          }
        },
      });
    } else {
      swal("Warning", "Please fill all field!!", "warning");
    }
  });
  $("#forgot").click(function () {
    flag = true;
    if ($("#tab3 #pas").val().trim() != $("#tab3 #cpas").val().trim()) {
      swal("Error", "Please enter same password in confirm password!!", "error");
      flag = false;
    } else {
      fl("#tab3 #email");
      fl("#tab3 #ans");
      fl("#tab3 #pas");
      fl("#tab3 #cpas");
      if (flag == false) {
          swal("Warning", "Please fill all field!!", "warning");
      }
    }
    if (flag) {
      if (confirm("Are you sure want to update password!!")) {
        $.ajax({
          method: "post",
          url: "pythonfile/login.py",
          data: {
            cond: "forgot",
            t1: $("#tab3 #email").val().trim(),
            t2: $("#tab3 #pas").val().trim(),
            t3: $("#tab3 #ans").val().trim(),
            t4: $("#tab3 #secq").val().trim(),
          },
          success: function (data) {
            data = data.split("&&");
            swal('Message',data[0],'info').then((value) => {
              location.reload()
            });
            // if (data[1] == 0) location.reload();
          },
        });
      }
    }
  });
});