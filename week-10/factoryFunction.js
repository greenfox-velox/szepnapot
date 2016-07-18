const dog = function() {
  const sound = 'woof';
  return {
    talk: function() {
      console.log(sound);
    }
  }
}

const sniffles = dog();
sniffles.talk();
