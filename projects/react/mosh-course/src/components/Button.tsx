type ButtonColor = "primary" | "secondary" | "dark";

interface Props {
  text: string;
  color?: ButtonColor;
  onClick: () => void;
}

function Button({ text, color = "primary", onClick }: Props) {
  return (
    <button
      type="button"
      className={"btn btn-" + color}
      onClick={() => {
        onClick();
      }}
    >
      {text}
    </button>
  );
}

export default Button;
