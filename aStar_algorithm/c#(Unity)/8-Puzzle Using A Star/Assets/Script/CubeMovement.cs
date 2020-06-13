using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CubeMovement : MonoBehaviour {
	public GameObject cubeManagerObj;
	
	[HideInInspector]
	public bool isOk_myPosition = true;
	[HideInInspector]
	public float next_x, next_z;
	[HideInInspector]
	public Vector3 endPosition;
	[HideInInspector]
	public Vector3 startPosition;
	private float speed = 2f;
	private Transform myPosition;
	
	void Start() {
		myPosition = gameObject.GetComponent<Transform>();
	}

	void Update () {
		float step = speed * Time.deltaTime;
		// Debug.Log(startPosition+" "+ endPosition);
		startPosition = transform.localPosition;
		if(!isOk_myPosition){
			myPosition.localPosition =  Vector3.MoveTowards(startPosition, endPosition, step);
		}
	}
}