//     *****************************************
//     СКРИПТ ДЛЯ МИНИ ИГРЫ
//     *****************************************
let user_answer = ['0', '0', '0'];
let counter = 0;

function contentMiniGame(data) {
  $('.js-game-not-ready').hide();
  $('.js-game-ready').show();
  $(".tic").removeClass("act");
  document.getElementById('mini-question').textContent = data.pictures[8].question;
  $('#0mini').attr("src", "/media/" + data.pictures[0].url);
  $('#1mini').attr("src", "/media/" + data.pictures[1].url);
  $('#2mini').attr("src", "/media/" + data.pictures[2].url);
  $('#3mini').attr("src", "/media/" + data.pictures[3].url);
  $('#4mini').attr("src", "/media/" + data.pictures[4].url);
  $('#5mini').attr("src", "/media/" + data.pictures[5].url);
  $('#6mini').attr("src", "/media/" + data.pictures[6].url);
  $('#7mini').attr("src", "/media/" + data.pictures[7].url);
  document.getElementById('try-number').textContent = data.number_of_try - 2;
}

function skipGame() {
  $.ajax({

    type: "GET",

    url: "/skip_mini_game/",

    dataType: 'json',

    cache: false,

    success: function (data) {
      if (data.bool) {
        $.ajax({
          type: "GET",

          url: "/next_mini_game/",

          dataType: 'json',

          cache: false,

          success: function (data) {
            checkStageMiniGame();
          }
        });
      }
    }
  });
}

function playerAction(elem, id) {
  if ($(elem).hasClass("act")) {
    $(elem).removeClass("act");
    user_answer[counter] = '0';
    if (counter > 0) {
      counter -= 1;
    }
  } else if (counter < 3) {
    $(elem).addClass("act");
    user_answer[counter] = parseInt(id,10);
    counter += 1;
  }

  if (counter === 3) {
    $.ajax({

      type: "GET",

      url: "/check_answer_for_game/",

      data: { 'user_answer1': user_answer[0],
              'user_answer2': user_answer[1],
              'user_answer3': user_answer[2]},

      dataType: 'json',

      cache: false,

      success: function (data) {
        if (data.bool) {
          $('.js-alert-success').addClass('game__alert_opacity-1');
          $.ajax({

            type: "GET",

            url: "/check_points/",

            dataType: 'json',

            cache: false,

            success: function (data) {
              document.getElementById('bonus').textContent = data.points;
              document.getElementById('bonus1').textContent = data.points;
            }
          });
          setTimeout(() => {
             $.ajax({

              type: "GET",

              url: "/next_mini_game/",

              dataType: 'json',

              cache: false,

              success: function (data) {
                $('.js-alert-success').removeClass('game__alert_opacity-1');
                checkStageMiniGame();
              }
            });
           }, 1000)
         
        } else {
          $('.js-alert-error').addClass('game__alert_opacity-1');
          setTimeout(() => {
            $.ajax({

              type: "GET",

              url: "/reload_mini_game/",

              dataType: 'json',

              cache: false,

              success: function (data) {
                $('.js-alert-error').removeClass('game__alert_opacity-1');
                checkStageMiniGame();
              }
            });
          }, 1000)
          
        }
      }
    });
  }
}

$(".tic").click(function(){
  let id = $(this).attr("id");
  let e = document.getElementById(id);
  playerAction(e,id);
});

function miniGameNotReady(time) {
  let constTime;
  $('.js-game-ready').hide();
  $('.js-game-not-ready').show();

  if (time === 'starttimer') {
    constTime = '29:59';
  } else {
    constTime = time.match(/\d*M\d*/g).toString().replace('M', ':');
  }

  function startTimer(timer) {
    if (timer !== undefined) {
      document.getElementById('js-timer').innerText = timer;
    }
    const elem = document.getElementById('js-timer');
    let tim = elem.innerText;
    let min = tim[0] + tim[1];
    let seconds = tim[3] + tim[4];
    if (seconds === '00') {
      if (min === '00') {
        $('.js-game-not-ready').hide();
      }
      min -= 1;
      seconds = '59';
      if (min < '10') min = '0' + min;
    } else {
      seconds -= 1;
    }
    if (seconds < 10) {
      seconds = '0' + seconds;
    }
    elem.textContent = min + ':' + seconds;
    setTimeout(startTimer, 1000);
  }
  startTimer(constTime);
}

function loadMiniGame() {
  $.ajax({

    type: "GET",

    url: "/load_picture/",

    dataType: 'json',

    cache: false,

    success: function (data) {
      if (data.pictures === 0) {
        miniGameNotReady(data.number_of_try);
      } else {
        contentMiniGame(data);
      }
    }
  });
}

function checkStageMiniGame() {
  counter = 0;
  $.ajax({
    type: "GET",
    url: "/check_game_is_ready/",
    cache: false,
    success: function(data){
      if (data.mini_game_is_ready === 1) {
        loadMiniGame();
      } else if (data.timer !== null) {
        miniGameNotReady(data.timer);
      } else {
        miniGameNotReady('starttimer');
      }
    }
  });
}

//     *****************************************




//     *****************************************
//     СКРИПТ ДЛЯ КОММЕНТАРИЕВ
//     *****************************************
function commentsData(objects) {
  for (let i = 0; i < objects.comments.length; i++) {
    document.getElementById("js-user" + i).innerText = objects.comments[i].user;
    document.getElementById("js-text" + i).innerText = objects.comments[i].text;
    document.getElementById("js-date" + i).innerText = objects.comments[i].date.match(/\d*-\d*-\d*/g);
    document.getElementById("js-city" + i).innerText = objects.comments[i].city;
    document.getElementById("js-rating" + i).innerText = objects.comments[i].rating;
    const element = document.getElementById('js-avatar' + i);
    $(element).attr("src", objects.comments[i].avatar);
  }
}

function loadComments() {
  $.ajax({
    type: "GET",
    url: "/get_comments/",
    cache: false, 
    success: function(data){
      commentsData(data);
    }
  });
}

function addComment() {
  $("#modalComment").modal();
}

//     *****************************************
function checkPoints() {
$.ajax({

    type: "GET",

    url: "/check_points/",

    cache: false,

    success: function (data) {
      document.getElementById('bonus').textContent = data.points;
      document.getElementById('bonus1').textContent = data.points;
    }
});
}

$(document).ready(function() {
  checkPoints();
  loadComments();
  checkStageMiniGame();

  var
    $window = $(window),
    $target = $("#panelbody"),
    $h = $target.offset().top;
    $window.on('scroll', function() {
  var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    if (scrollTop > $h) {
      $("#panelbody1").addClass("show_block");
    } else {
      $("#panelbody1").removeClass("show_block");
    }
  });
});
