public class ObserverTest {

  public static void main(String[] args) {
    ConcreteSubject subject = new ConcreteSubject();
    ConcreteObserver observer1 = new ConcreteObserver("Observer1");
    ConcreteObserver observer2 = new ConcreteObserver("Observer2");

    subject.attach(observer1);
    subject.attach(observer2);
    subject.setState(1);

    subject.detach(observer1);
    subject.setState(2);
  }
}
