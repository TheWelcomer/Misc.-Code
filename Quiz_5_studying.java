public class Quiz_5_studying {
    public E pop() {
        if
        head = head.next
    }
}
public static void reverse(Stack s) {
    Queue q = new LinkedList();
    while(!(s.isEmpty())) {
        q.add(s.pop());
    }
    while(!(q.isEmpty())) {
        s.push(q.remove());
    }
}

public void push(E e) {
    if (isFull()) {
        enlarge();
    }
    top += 1;
    array[top] = e;
}

void enlarge() {
    String[] larger = new String[array.length * 2];
    for (int i = 0; i < array.length; i++) {
        larger[i] = array[i];
    }
    array = larger;
}
