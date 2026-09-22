import java.util.ArrayList;
import java.util.List;

public class ConcreteSubject implements Subject {

  private List<Observer> observers = new ArrayList<Observer>();
  private int state;

  public void attach(Observer observer) {
    observers.add(observer);
  }

  public void detach(Observer observer) {
    observers.remove(observer);
  }

  public void notifyObservers() {
    for (Observer observer : observers) {
      observer.update(state);
    }
  }

  public void setState(int state) {
    this.state = state;
    notifyObservers();
  }

  public int getState() {
    return state;
  }
}
