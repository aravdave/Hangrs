import React from 'react';
import {
  Text,
  StyleSheet,
} from 'react-native';

export const OurText = (props) => {
    return (
      <Text style={[styles.text, props.style]}>
        {props.children}
      </Text>
    );
}

const styles = StyleSheet.create({
  text: {
    fontFamily: "Roboto",
  },
});