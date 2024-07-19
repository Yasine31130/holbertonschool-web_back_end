export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = HolbertonCourse.validateString(name, 'Name');
    this._length = HolbertonCourse.validateNumber(length, 'Length');
    this._students = HolbertonCourse.validateArray(students, 'Students');
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    this._name = HolbertonCourse.validateString(newName, 'Name');
  }

  get length() {
    return this._length;
  }

  set length(newLength) {
    this._length = HolbertonCourse.validateNumber(newLength, 'Length');
  }

  get students() {
    return this._students;
  }

  set students(newStudents) {
    this._students = HolbertonCourse.validateArray(newStudents, 'Students');
  }

  static validateString(value, propertyName) {
    if (typeof value !== 'string') {
      throw new TypeError(`${propertyName} must be a string`);
    }
    return value;
  }

  static validateNumber(value, propertyName) {
    if (typeof value !== 'number') {
      throw new TypeError(`${propertyName} must be a number`);
    }
    return value;
  }

  static validateArray(value, propertyName) {
    // Checking that the value is an array and that every element in it is a string
    if (!Array.isArray(value) || !value.every((student) => typeof student === 'string')) {
      throw new TypeError(`${propertyName} must be an array`);
    }
    return value;
  }
}
