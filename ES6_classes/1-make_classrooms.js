/* eslint-disable import/extensions */
import ClassRoom from './0-classroom.js';

export default function initializeRooms() {
  // map() applies a callback function to each element in the array
  return [19, 20, 34].map((size) => new ClassRoom(size));
}
