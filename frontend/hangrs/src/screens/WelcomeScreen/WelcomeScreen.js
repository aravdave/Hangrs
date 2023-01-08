import React, {useState} from 'react';
import CheckBox from '@react-native-community/checkbox';
import { OurText } from '../../components/OurText';
// import styles from '../StylesSheet.js'
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  Image,
  TextInput,
  TouchableOpacity,
  useColorScheme,
  View,
  AppRegistry
} from 'react-native';

export default function WelcomeScreen() {

  function signIn() {

  }

  return (
    <View style={styles.container}>
      <View style={styles.heading}>
        <Text style={styles.headingText}>
          Welcome to hangrs!
        </Text>
      </View>
      <View style={styles.backgroundImageContainer}>
        <Image
          style={styles.backgroundImage}
          source={require('C:/Users/aravd/Documents/Hangrs/frontend/hangrs/assets/placeholder_image.png')}
        />
      </View>
      <View style={styles.userInput}>
        <TouchableOpacity
          style={styles.signUpButton}
          activeOpacity={0.7}
        >
          <OurText style={styles.signUpText}>
            Join us
          </OurText>
        </TouchableOpacity>
        <TouchableOpacity
          style={styles.signInButton}
          activeOpacity={0.7}
        >
          <OurText style={styles.signInText}>
            Log in
          </OurText>
        </TouchableOpacity>
      </View>
    </View>
  )
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#101820FF",
  },
  heading: {
    flex: 2,
    justifyContent: "center",
    alignItems: "center",
  },
  headingText: {
    fontSize: 30,
    fontWeight: "bold",
    color: "#006B38FF",
  },
  backgroundImageContainer: {
    flex: 3,
    alignItems:"center",
  },
  backgroundImage: {
    width: 300,
    height: 300,
  },
  userInput: {
    flex: 2,
    justifyContent:"center",
    alignItems: "center",
  },
  signUpButton: {
    padding: 10,
    width: "60%",
    height: "30%",
    marginTop: 30,
    marginBottom: 15,
    borderRadius: 15,
    borderWidth: 4,
    borderColor: "#006B38FF",
    backgroundColor: "#006B38FF",
    alignItems: "center",
  },
  signUpText: {
    fontSize: 20,
    fontWeight: "bold",
    color: "#101820FF",
  },
  signInButton: {
    padding: 10,
    width: "60%",
    height: "30%",
    marginBottom: 15,
    borderRadius: 15,
    borderWidth: 4,
    borderColor: "#006B38FF",
    backgroundColor: "#101820FF",
    alignItems: "center",
  },
  signInText: {
    fontSize: 20,
    fontWeight: "bold",
    color: "#006B38FF",
  },
});