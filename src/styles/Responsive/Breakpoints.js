const size = {
  break1: 425,
  break2: 800,
  break3: 1200,
};

export const Breakpoints = {
  break1: `(max-width: ${size.break1}px)`,
  break2: `(min-width: ${size.break1}px) and (max-width: ${size.break2}px)`,
  break3: `(min-width: ${size.break2}px) and (max-width: ${size.break3}px)`,
  break4: `(min-width: ${size.break3}px)`,
};
export default Breakpoints;
