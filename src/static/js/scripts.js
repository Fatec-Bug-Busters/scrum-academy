function toggleText(container) {
    container.classList.toggle('active');
}

// Script Login
$(document).ready(function () {
    $('#loginForm').submit(function (event) {
      event.preventDefault();
      var formData = {
        'email': $('#email').val(),
      };

      var email = ($("#email").val())
      $.ajax({
        type: 'POST',
        url: '/login',
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function (response) {
          $('#message').html(response.message);
          if (response.success) {
            $('#ModalLogin').modal('hide');
            $('#ModalLoginSucess').modal('show');
            setTimeout(function () {
              window.location.reload();
            }, 2000)
          } else {

            $('#ModalLogin').modal('hide');
            $('#ModalNewUser').modal('show');
          }
        },
        error: function (error) {
          console.log(error);
          $('#ModalLogin').modal('hide');
          $('#ModalError').modal('show');
        }
      });
    });
  });

  // Script New User
  $(document).ready(function () {
    $('#NewUserForm').submit(function (event) {
      event.preventDefault();
      var formData = {
        'email': $('#email').val(),
        'NameUser': $('#NameUser').val()
      };
      $.ajax({
        type: 'POST',
        url: '/register',
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function (response) {
          $('#ModalNewUser').modal('hide');
          $('#ModalLoginSucess').modal('show');
          setTimeout(function () {
            window.location.reload();
          }, 2000)
        },
        error: function (error) {
          console.log(error);
          $('#ModalNewUser').modal('hide');
          $('#ModalIncompleteName').modal('show');
          setTimeout(function () {
            $('#ModalIncompleteName').modal('hide');
            $('#ModalNewUser').modal('show');
          }, 1500)
        }
      });
    });
  });
  // Script Logout
  $(document).ready(function () {
    $('#btn_logout').click(function () {
      $.ajax({
        type: 'POST',
        url: '/logout',
      });
      window.location.reload();
    });
  });