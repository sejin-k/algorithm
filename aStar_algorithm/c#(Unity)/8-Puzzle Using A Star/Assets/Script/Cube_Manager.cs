using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Cube_Manager : MonoBehaviour {
	public GameObject cubes;
	public GameObject gameManager;

	private GameObject[,] cubesPosition;
	private aStar_Manager aStar;
	private List<int[]> seq_path;
	private int[,] state;
	private float distanceRatio = 2.25f;

	void Start () {
		Debug.Log("Start Cube Manager");
		aStar = gameManager.GetComponent<aStar_Manager>();
		this.state = aStar.get_start_state();	

		set_cubes();
		set_initPosition();
		this.seq_path = aStar.SequenceOfpath();	//aStar.sample;

		StartCoroutine("move");
	}
	
	// 8개 cube들 시작 위치로 이동
	public void set_initPosition() {
		for(int h = 0; h < this.cubesPosition.GetLength(0); h++) {
			for(int w = 0; w < this.cubesPosition.GetLength(1); w++) {
				if(this.cubesPosition[h,w] == null) {
					continue;
				}
				else {
					cubesPosition[h,w].GetComponent<Transform>().position = new Vector3((w-1)*distanceRatio,cubesPosition[h,w].GetComponent<Transform>().position.y,(1-h)*distanceRatio);
				}
			}
		}
	}

	// state에 맞게 큐브 배치.
	public void set_cubes() {
		this.cubesPosition = new GameObject[this.state.GetLength(0), this.state.GetLength(1)];

		for(int h = 0; h < this.state.GetLength(0); h++) {
			for(int w = 0; w < this.state.GetLength(1); w++) {
				if(this.state[h,w] == -1) {
					cubesPosition[h,w] = null;
				}
				else {
					cubesPosition[h,w] = cubes.transform.GetChild(this.state[h,w] - 1).gameObject;
				}
			}
		}
	}

	// cube 움직임을 위한 coroutione
	IEnumerator move() {
		CubeMovement temp;

		for(int i = 0; i < seq_path.Count - 1; i++) {
			temp = cubesPosition[seq_path[i+1][1], seq_path[i+1][0]].GetComponent<CubeMovement>();
			temp.next_x = (1 - seq_path[i][0]) * distanceRatio;
			temp.next_z = (seq_path[i][1] - 1) * distanceRatio;
			// Debug.Log(cubesPosition[seq_path[i+1][1], seq_path[i+1][0]].name);
			// Debug.Log(temp.next_x+" , "+temp.next_z);
			temp.endPosition = new Vector3(temp.next_x, 0, temp.next_z);
			temp.isOk_myPosition = false;
			cubesPosition[seq_path[i][1], seq_path[i][0]] = cubesPosition[seq_path[i+1][1], seq_path[i+1][0]];
			cubesPosition[seq_path[i+1][1], seq_path[i+1][0]] = null;
			yield return new WaitForSeconds(1.0f);
		}
	}
}
