
var countDownDate = new Date("2 10 3000 21:0:0").getTime();
            var x = setInterval(function () {
              var now = new Date().getTime();
              var distance = countDownDate - now;
              var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
              var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
              var seconds = Math.floor((distance % (1000 * 60)) / 1000);
              document.getElementById("demo").innerHTML = hours + "h "
                + minutes + "m " + seconds + "s ";
              if (distance < 0) {
                clearInterval(x);
                document.getElementById("demo").innerHTML = "EXPIRED";
              }
            }, 1000);