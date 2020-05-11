public class Shape {

	protected int cost;

	public Shape() {
		cost = 5;
	}

	public void talk() {

		System.out.println(cost);

		int cost = 600;
		System.out.println(cost);		
	}

	public int getCost() {
		return cost;
	}
}