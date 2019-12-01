package POO;

// import java.util.Scanner;

public class Conta {

	private String numero;
	private float saldo;
	// private Scanner input = new Scanner(System.in);

	//saque
	//saldo
	//deposito

	Conta () {}
	Conta (String numero, float saldo) {
		this.numero = numero;
		this.saldo = saldo;
	}

	public String getNumero() {
		return this.numero;
	}

	public float getSaldo() {
		return this.saldo;
	}

	public void setNumero(String numero) {
		this.numero = numero;
	}

	public void setSaldo(float saldo) {
		this.saldo = saldo;
	}

	public float saldo() {
		return this.getSaldo();
	}

	public void saque(float valor) {
		if (valor <= this.getSaldo() && valor > 0) {
			this.setSaldo(this.getSaldo()-valor);
		}
	}

	public void deposito(float valor) {
		if (valor > 0) {
			this.setSaldo(this.getSaldo()+valor);
		}
	}

}