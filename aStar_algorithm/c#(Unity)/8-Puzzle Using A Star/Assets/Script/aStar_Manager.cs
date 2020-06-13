using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class aStar_Manager : MonoBehaviour {
	private A_star algorithm;
	private int[,] start_state = new int[3,3];
	private int[,] goal_state = new int[3,3] {{1,2,3},{4,5,6},{7,8,-1}};
	public int[,] sample = new int[3,3] {{-1,1,3},{4,2,6},{7,5,8}};

	void Awake () {
		create_random_state();
		set_start_goal_state();
		this.algorithm.main();
		path2Text();
	}

	// start와 goal state를 정해준다.
	public void set_start_goal_state() {
		this.algorithm = gameObject.GetComponent<A_star>();
		this.algorithm.start_state = this.start_state;	//this.sample;
		this.algorithm.goal_state = this.goal_state;
	}

	// random state를 생성하여 start에 넣어준다.
	public void create_random_state() {
		List<int> basic = new List<int>() {1,2,3,4,5,6,7,8,-1};
		int[] shuffle = new int[9];
		int c = basic.Count;

		for (int i = 0; i < c; i++){
			int rand = Random.Range(0, basic.Count);
			shuffle[i] = basic[rand];
			basic.RemoveAt(rand);
		}

		for (int n=0, j=0; n<this.start_state.GetLength(0); n++){
			for (int m=0; m<this.start_state.GetLength(1); m++, j++){
				this.start_state[n,m] = shuffle[j];
			}
		}

		Debug.Log("################ Start State ################");
		print_state(this.start_state);
	}

	// state의 상태를 출력해준다(디버깅, 중간 state 확인)
	public string print_state(int[,] s) {
		string str = "\n\t";

		for (int h=0; h<s.GetLength(0); h++){
			for(int w=0; w<s.GetLength(1); w++){
				str += s[h,w] + "\t";
			}
			str += "\n\t";
		}
		Debug.Log(str);
		return str;
	}

	// 중간 state값을 txt 파일로 저장.
	public void path2Text() {
		string savePath = @"C:\Users\Allpath.txt";
		string textValue = "";
		List<int[,]> path = algorithm.path;

		Debug.Log("################ result path ################");
		for(int i = 0; i < path.Count; i++) {
			textValue += "Sequence of path : " + (i + 1).ToString();
			if(i == 0 || i == (path.Count - 1)) {
				if(i == 0) {
					textValue += "\t(Start)";
				}
				else {
					textValue += "\t(Goal)";
				}
			}
			textValue += print_state(path[i]) + "\n";
		}

		System.IO.File.WriteAllText(savePath, textValue);
	}

	// 다른 script에서 start state를 얻기위한 get
	public int[,] get_start_state() {
		return this.start_state;
	}

	// 최종 길로 가기위한 path를 좌표로 변환하여 저장
	public List<int[]> SequenceOfpath() {
		List<int[]> seq_path = new List<int[]>();

		foreach(int[,] p in algorithm.path) {
			seq_path.Add(algorithm.find_blank_pos(p));
		}

		return seq_path;
	}
}
