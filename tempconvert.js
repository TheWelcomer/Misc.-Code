function convertTemp(input, inputFlag, outputFlag) {
    var output;
    if (inputFlag === '-f') {
    if (outputFlag === '-c') {
      output = (input - 32) * 5 / 9;
    } else if (outputFlag === '-k') {
      output = (input + 459.67) * 5 / 9;
    } else {
        output = input;
    }
    } else if (inputFlag === '-c') {
    if (outputFlag === '-f') {
      output = input * 9 / 5 + 32;
    } else if (outputFlag === '-k') {
      output = input + 273.15;
    } else {
      output = input;
    }
  } else if (inputFlag === '-k') {
    if (outputFlag === '-f') {
      output = input * 9 / 5 - 459.67;
    } else if (outputFlag === '-c') {
      output = input - 273.15;
    } else {
      output = input;
    }
  }
  return output;
}

console.log(convertTemp(1091, '-c', '-k'));