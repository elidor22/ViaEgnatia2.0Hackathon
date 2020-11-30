import React from "react";
import ImageInput from "./ImageInput";
import ProcessedImage from "./ProcessedImage";
import Header from "../components/Header";
import Footer from "../components/Footer";
import { connect } from "react-redux";

class Main extends React.Component {
  render() {
    const checker = (yes) => {
      if (yes === null) {
        return <ImageInput />;
      } else return <ProcessedImage />;
    };
    return (
      <div className="container text-center">
        <Header />
        {checker(this.props.fetchAIReduce)}
        <Footer/>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  console.log(state);
  return {
    fetchAIReduce: state.fetchAI,
  };
};

export default connect(mapStateToProps)(Main);
