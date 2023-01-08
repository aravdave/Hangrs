/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

import React, {useState} from 'react';
import CheckBox from '@react-native-community/checkbox';
import styles from '../StylesSheet.js'
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


export default function SignUpScreen() {
  
  const [formData, setFormData] = useState({
        firstName: "",
        lastName: "",
        username: "",
        password: "",
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
      <View style={[styles.box, {height: 500}]}>
        <Text style={styles.header}>Sign Up</Text>
        <View style={styles.signUp}>
          <Text style={styles.text}>Already an user?</Text>
          <Text style={styles.link}>Sign In</Text>
        </View>
        <TextInput
          style={styles.input}
          value={formData.firstName}
          placeholder="First Name"
          onChangeText={text => handleChange('firstName', text)}
        />  
        <TextInput
          style={styles.input}
          value={formData.lastName}
          placeholder="Last Name"
          onChangeText={text => handleChange('lastName', text)}
        />
        <TextInput
          style={styles.input}
          value={formData.username}
          placeholder="Username or email"
          onChangeText={text => handleChange('username', text)}
        />
        <TextInput
          style={styles.input}
          value={formData.password}
          secureTextEntry={true}
          placeholder="Password"
          onChangeText={text => handleChange('password', text)}
        />

        <TouchableOpacity
          style={styles.button}
          activeOpacity={0.7}
          onPress={handleSubmit}
        >
          <Text style={styles.text}>Sign Up</Text>
        </TouchableOpacity>

        <View style={styles.orSignUpWith}>
          <View style={styles.horizontalLine} />
          <Text style={{ alignSelf:'center', paddingHorizontal: 35, fontSize: 15 }}>Or Sign Up With</Text>
          <View style={styles.horizontalLine} />
        </View>

        
      </View>             
    </View>
  )
};

// const styles = StyleSheet.create({
//   container: {
//     flex:1,
//     justifyContent: 'center',
//     alignItems: 'center',
//     backgroundColor: '#1c1c1c',
//   },
//   box: {
//     justifyContent: 'center',
//     alignItems: 'center',
//     width: 300,
//     height: 400,
//     backgroundColor: "white",
//     borderRadius:10,
//   },
//   logo: {
//     color: 'cornsilk',
//     fontSize: 12,
//     padding:1,
//   },
//   input: {
//     fontFamily: "Inter",
//     fontWeight: "bold",
//     borderRadius: 5,
//     borderColor: 'gray',
//     backgroundColor: 'white',
//     borderWidth:2,
//     margin: 10,
//     paddingLeft: 15,
//     width: 200,
//   },
//   button: {
//     borderRadius: 4,
//     backgroundColor: '#4ADE80',
//   },
//   signUp: {
//     flexDirection:"row",
//     justifyContent:"space-evenly",
//   },
//   header: {
//     color: "black",
//     fontSize: 25,
//     fontFamily: "normal",
//     margin: 5,
//     paddingBottom: 10,
//   },
//   signIn: {
//     color: "black",
//     alignSelf:"center",
//     fontSize: 12,
//     padding: 10,
//   },
//   text: {
//     color: "black",
//     fontSize: 15,
//     padding: 10,
//   },
//   link: {
//     color: "dodgerblue",
//     fontSize: 15,
//     padding: 10,
//   },
//   staySignedIn: {
//     flexDirection:"row",
//     justifyContent:"flex-start",
//     width:220,
//     alignItems:"center",
//     padding: 3,
//   },
// });