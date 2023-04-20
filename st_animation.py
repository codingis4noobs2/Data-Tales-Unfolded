typing_animation_html = '''
<div class="typewriter">
  <h1>Data Tales Unfolded!📊📈📉</h1>
</div>
'''

typing_animation_css = '''
<style>
.typewriter {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50%; /* Update to percentage value */
}

.typewriter h1 {
  overflow: hidden;
  border-right: .15em solid orange;
  white-space: nowrap;
  margin-top: 1%; /* Update to percentage value */
  margin-bottom: 5%;
  letter-spacing: .15em;
  animation:
    typing 3.5s steps(40, end),
    blink-caret .75s step-end infinite;
}


@keyframes typing {
  from {
    width: 0
  }
  to {
    width: 100%
  }
}

@keyframes blink-caret {
  from,
  to {
    border-color: transparent
  }
  50% {
    border-color: orange
  }
}
</style>
'''

typing_animation_js = '''
<script>
document.addEventListener('DOMContentLoaded', function(event) {
  var i = 0;
  var txt = 'Data Tales Unfolded!📊📈📉';
  var speed = 100; /* The speed/duration of the typing effect in milliseconds */

  function typeWriter() {
    if (i < txt.length) {
      document.querySelector('.typewriter h1').textContent += txt.charAt(i);
      i++;
      setTimeout(typeWriter, speed);
    }
  }

  typeWriter();
});
</script>
'''