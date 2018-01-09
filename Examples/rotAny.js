const rotAny = (input, rotation) => input.split('').map((character) => {
  const upperCase = character === character.toUpperCase();
  const initial = character.toLowerCase().charCodeAt();
  if (initial >= 97 && initial <= 122) {
    const rotated = String.fromCharCode(((initial + (rotation - 97)) % 26) + 97);
    return upperCase ? rotated.toUpperCase() : rotated;
  } return character;
}).join('');
