// RxJS v6+
import { empty } from 'rxjs';

//output: 'Complete!'
const subscribe = empty().subscribe({
  next: () => console.log('Next'),
  complete: () => console.log('Complete!')
});