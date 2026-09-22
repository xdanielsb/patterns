public class ConcreteObserver implements Observer {

  private String name;

  public ConcreteObserver(String name) {
    this.name = name;
  }

  public void update(int state) {
    System.out.println(name + " has been updated: " + state);
  }
}
