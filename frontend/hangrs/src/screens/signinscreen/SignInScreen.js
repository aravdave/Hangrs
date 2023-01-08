/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

import React, {useState} from 'react';
import CheckBox from '@react-native-community/checkbox';
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  useColorScheme,
  View,
  AppRegistry
} from 'react-native';


export default function SignInScreen() {
  
  const [formData, setFormData] = useState({
        username: "",
        password: "",
        staySignedIn: false,
  })

  function handleChange(name, value) {
    setFormData(prevFormData => ({
      ...prevFormData,
      [name]: value,
    }))
  }

  function handleSubmit() {
    /* Encrypt password and make API call to django backend */
  }

  return (
    <View style={styles.container}>
      <View style={styles.box}>
        <Text style={styles.header}>Sign In</Text>
        <View style={styles.signUp}>
          <Text style={styles.text}>New user?</Text>
          <Text style={styles.link}>Create an account</Text>
        </View>
        <TextInput
          style={styles.input}
          value={formData.username}
          placeholder="Username or email"
          onChangeText={text => handleChange('username', text)}
        />  
        <TextInput
          style={styles.input}
          value={formData.password}
          placeholder="Password"
          secureTextEntry={true}
          onChangeText={text => handleChange('password', text)}
        />
        <View style={styles.staySignedIn}>
          <CheckBox
            value={formData.staySignedIn}
            onValueChange={(newState) => handleChange('staySignedIn', newState)}
          />
          <Text styles={styles.text}>Keep me signed in</Text>
        </View>
        <TouchableOpacity
          style={styles.button}
          activeOpacity={0.7}
          onPress={handleSubmit}
        >
          <Text style={styles.text}>Sign In</Text>
        </TouchableOpacity>
      </View>             
    </View>
  )
};

const styles = StyleSheet.create({
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
});