import {StyleSheet} from 'react-native';
import react from 'react';


export default styles = StyleSheet.create({
  container: {
    flex:1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#1c1c1c',
  },
  box: {
    justifyContent: 'center',
    alignItems: 'center',
    width: 300,
    height: 400,
    backgroundColor: "white",
    borderRadius:10,
  },
  logo: {
    color: 'cornsilk',
    fontSize: 12,
    padding:1,
  },
  input: {
    fontFamily: "Inter",
    fontWeight: "bold",
    borderRadius: 5,
    borderColor: 'gray',
    backgroundColor: 'white',
    borderWidth:2,
    margin: 10,
    paddingLeft: 15,
    width: 200,
  },
  button: {
    borderRadius: 4,
    backgroundColor: '#4ADE80',
    marginTop: 18,
  },
  signUp: {
    flexDirection:"row",
    justifyContent:"space-evenly",
  },
  header: {
    color: "black",
    fontSize: 25,
    fontFamily: "normal",
    margin: 5,
    paddingBottom: 10,
  },
  signIn: {
    color: "black",
    alignSelf:"center",
    fontSize: 12,
    padding: 10,
  },
  text: {
    color: "black",
    fontSize: 15,
    padding: 10,
  },
  link: {
    color: "dodgerblue",
    fontSize: 15,
    padding: 10,
  },
  staySignedIn: {
    flexDirection:"row",
    justifyContent:"flex-start",
    width:220,
    alignItems:"center",
    padding: 3,
  },  
  orSignUpWith: {
    flexDirection: "row",
    justifyContent: "space-around",
    width: 300,
    paddingHorizontal : 35,
    paddingVertical : 18,
  },
  horizontalLine: {
    backgroundColor: 'lightgray',
    height: 2,
    alignSelf: 'center',
    width: 50,
  },
});