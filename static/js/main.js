$(function() {

  var app_id = '1682310898660786';
  var scopes = 'public_profile, email, user_friends';

  var btn_login = '<a href="#" id="login" class="btn btn-primary">Iniciar sesión  <i class="fa fa-facebook" aria-hidden="true"</a>';

  var div_session = "<div id='facebook-session'>"+
            "<a href='#' id='logout' class='btn btn-danger'>Cerrar sesión</a>"+
            "</div>";

  window.fbAsyncInit = function() {

      FB.init({
        appId      : '1626325910991457',
        status     : true,
        cookie     : true, 
        xfbml      : true, 
        version    : 'v2.6'
      });


      FB.getLoginStatus(function(response) {
        statusChangeCallback(response, function() {});
      });
    };

    var statusChangeCallback = function(response, callback) {
      console.log(response);
      
      if (response.status === 'connected') {
          getFacebookData();
      } else {
        callback(false);
      }
    }
    
    var checkLoginState = function(callback) {
      FB.getLoginStatus(function(response) {
          callback(response);
      });
    }
    var getFacebookData =  function() {
      FB.api('/me', function(response) {
        $('#login').after(div_session);
        $('#login').remove();
        $('#logout').text(response.name+" (Cerrar Sesión)");
      });
    }

    var facebookLogin = function() {
      checkLoginState(function(data) {
        if (data.status !== 'connected') {
          FB.login(function(response) {
            if (response.status === 'connected')
              getFacebookData();
          }, {scope: scopes});
        }
      })
    }

    var facebookLogout = function() {
      checkLoginState(function(data) {
        if (data.status === 'connected') {
          FB.logout(function(response) {
            $('#facebook-session').before(btn_login);
            $('#facebook-session').remove();
          })
        }
      })
    }

    $(document).on('click', '#login', function(e) {
      e.preventDefault();

      facebookLogin();
    })

    $(document).on('click', '#logout', function(e) {
  
      e.preventDefault();

      if (confirm("¿Está seguro?"))
        facebookLogout();
      else 
        return false;
    })

})